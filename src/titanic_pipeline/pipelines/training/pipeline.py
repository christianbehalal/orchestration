from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_data, train_model, evaluate_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_data,
            inputs="titanic",
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="preprocess_data_node"
        ),
        node(
            func=train_model,
            inputs=["X_train", "y_train"],
            outputs="model",
            name="train_model_node"
        ),
        node(
            func=evaluate_model,
            inputs=["model", "X_test", "y_test"],
            outputs="predictions_vs_truth",  # ✅ correspond au catalog.yml
            name="evaluate_model_node"
        ),
    ])
