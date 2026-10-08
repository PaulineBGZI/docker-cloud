# Utilise Python 3.12 avec Alpine Linux comme image de base légère
FROM python:3.12-alpine

# Définit /app comme dossier de travail dans le conteneur
WORKDIR /app

# Copie le fichier contenant les dépendances Python
COPY requirements.txt .

# Installe les dépendances nécessaires au backend
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code de l'application dans le conteneur
COPY app.py .

# Copie les données du catalogue dans le conteneur
COPY data ./data

# Indique que l'application Flask utilise le port 5000
EXPOSE 5000

# Lance l'application Flask au démarrage du conteneur
CMD ["python", "app.py"]
