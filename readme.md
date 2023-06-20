## Contexte du projet

En tant que développeur, afin de développer une application maintenable dans le temps il est nécessaire pour l'équipe de développement de définir et mettre en place une série de test unitaire pouvant être joué de manière automatisé. L'utilisation de la TDD peut être aussi un avantage non négligeable pour le développement d'une application.

​

Dans ce premier briefs nous mettrons en place un serveur d'API simple sur lequel nous réaliserons nos premiers tests côtés backend.

​

Il est à noté que sur ces exercices les technologies seront impoisées mais la philosophie de tests restera la même et est transposable à toutes les technologies.

## Technologies

Backend : Python
Framework : Django

## Setup 
Créer un environement virtuel:
    
    py -m venv .venv

Lancer l'environement virutal:
- Linux:

        source .venv/bin/activate

- Windows:

        .venv/Script/activate.bat



Installer les dépendances:

    pip install -r requirements.txt

Lancer les migrations

    cd src
    python manage.py makemigrations unitTest
    python manage.py migrate

Lancer le projet:

    python manage.py runserver

## Docker
    docker-compose up

Se rendre sur l'url http://localhost:8000

## Test Unitaire
    Py manage.py test

## Endpoint
**Game Endpoints :**

**`GET /game/`** : Récupère la liste de toutes les jeux.

**`POST /game/`** : Crée un nouveau.

**`GET /game/{id}/`** : Récupère les détails d'un jeu.

**`PUT /game/{id}/`** : Met à jour le ou les information d'un jeu.

`PATCH /game/{id}/`** : Met à jour une information sur un jeu.

`DELETE /game/{id}/`** : Supprime un jeu.