# TP Docker Cloud

Le thème choisi pour le projet est un **mini catalogue de cookies**.

Le projet permet d'afficher une liste de cookies récupérée depuis une API, le tout dans une architecture composée de plusieurs conteneurs Docker.

## Services

Le projet contient trois services :

- `front` : interface du catalogue
- `back` : API contenant les données des cookies
- `proxy` : point d'entrée de l'application

La documentation détaillée de l'architecture est disponible dans [`docs/architecture.md`](docs/architecture.md).

## Technologies

- HTML / CSS / JavaScript
- Nginx
- Python 3.12
- Flask
- Docker
- Docker Compose

## Structure du projet

```text
docker-cloud/
├── front/
│   ├── Dockerfile
│   ├── index.html
│   └── style.css
├── back/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── web-server/
│   ├── Dockerfile
│   └── nginx.conf
├── docs/
│   └── architecture.md
├── docker-compose.yml
└── README.md
```

## Lancement

Construire les images et démarrer les services :

```bash
docker compose up --build
```

L'application est ensuite accessible sur :

```text
http://localhost:8080
```

L'API peut également être consultée directement via le proxy :

```text
http://localhost:8080/api/
```

## Arrêt

Arrêter et supprimer les conteneurs créés par Docker Compose :

```bash
docker compose down
```