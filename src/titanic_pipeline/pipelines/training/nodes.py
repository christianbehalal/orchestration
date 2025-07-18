import pandas as pd
import logging
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report


def preprocess_data(data: pd.DataFrame):
    """Nettoie, encode, et sépare les données en ensembles d'entraînement et de test."""

    # Supprimer des colonnes inutiles
    data = data.drop(columns=["deck", "embark_town", "alive", "who", "adult_male", "class"], errors="ignore")

    # Supprimer les lignes avec des NaNs importants
    data = data.dropna(subset=["embarked", "age", "fare", "sex", "survived"])

    # Encoder les colonnes catégorielles
    for col in ["sex", "embarked"]:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])

    # Séparer les features et la cible
    X = data.drop(columns=["survived"])
    y = data["survived"]

    # Séparation en jeu d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Convertir y en DataFrame pour compatibilité Kedro
    y_train = y_train.to_frame()
    y_test = y_test.to_frame()

    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.DataFrame):
    """Entraîne un modèle de régression logistique et log dans MLflow automatiquement."""

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X_train, y_train.values.ravel())

    # Log du modèle et des paramètres dans MLflow (géré automatiquement par Kedro-MLflow)
    mlflow.sklearn.log_model(pipeline, "model")
    mlflow.log_param("model_type", "logistic_regression")
    mlflow.log_param("standard_scaler", True)
    mlflow.log_metric("train_score", pipeline.score(X_train, y_train))

    return pipeline


def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.DataFrame) -> pd.DataFrame:
    """Évalue le modèle, loggue dans MLflow, et retourne un DataFrame complet avec prédictions."""

    # Copie les features originales
    full_features = X_test.copy()

    # Prédictions
    y_pred = model.predict(X_test)
    y_true = y_test.values.ravel()

    # Log dans MLflow
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred)

    logger = logging.getLogger(__name__)
    logger.info(f"Accuracy: {accuracy:.4f}")
    logger.info("Classification Report:\n" + report)

    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_text(report, "classification_report.txt")

    # Ajouter les colonnes de comparaison
    full_features["y_true"] = y_true
    full_features["y_pred"] = y_pred

    return full_features
