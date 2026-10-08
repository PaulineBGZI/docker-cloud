# TP Docker Cloud

Le thème choisi pour le projet est un **mini catalogue de cookies**.

Le projet permet d'afficher un catalogue de cookies récupéré depuis une API, avec une page d'accueil, une page catalogue et une page de détail pour chaque cookie.

## Services

Le projet contient trois services :

- `front` : interface web du catalogue
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
│   ├── catalogue.html
│   ├── cookie.html
│   ├── style.css
│   └── images/
│       ├── chocolat.png
│       ├── 3choco.png
│       ├── caramel.png
│       ├── noisette.png
│       ├── choco-blanc.png
│       ├── speculos.png
│       ├── pistache.png
│       ├── framboise.png
│       └── coco.png
├── back/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── data/
│       └── cookies.json
├── web-server/
│   ├── Dockerfile
│   └── nginx.conf
├── docs/
│   └── architecture.md
├── .env
├── .gitignore
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
