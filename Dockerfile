# Utiliser une image de base Python
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances du projet
RUN pip install -r requirements.txt

# Copier le contenu du répertoire courant dans le conteneur
COPY ./src /app

# Exposer le port 8000 (le port sur lequel Django s'exécute par défaut)
EXPOSE 8000

# Exécuter la commande pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
