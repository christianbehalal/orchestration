# Utilise une image Python officielle
FROM python:3.9-slim

# Crée le dossier de travail
WORKDIR /app

# Copie les fichiers de ton repo dans le conteneur
COPY . .

# Installe les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Spécifie le port que Flask utilisera
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "api/app.py"]
