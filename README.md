# TP Docker Cloud

Le thème choisi pour le projet est un **mini catalogue de cookies**.

## Architecture

Le projet est composé de trois services :

- `front` : interface web avec Nginx
- `back` : API développée en Python avec Flask
- `proxy` : serveur Nginx utilisé comme reverse proxy entre l’utilisateur, le frontend et le backend

Schéma :

## Technologies utilisées

### Frontend

- HTML
- Nginx Alpine

J'ai choisi Nginx Alpine car ça permet d'avoir une image légère.

### Backend

- Python 3.12
- Flask
- Alpine Linux

Le backend expose une API HTTP utilisée pour fournir les données du catalogue de cookies.

### Proxy

- Nginx Alpine

Le proxy reçoit les requêtes HTTP et les redirige vers le frontend ou le backend selon l’URL utilisée.

## Ressources

| Service | Mémoire | CPU |
|---|---:|---:|
| Front | 128 MiB | 0.25 |
| Back | 256 MiB | 0.50 |
| Proxy | 128 MiB | 0.25 |

Le backend possède plus de ressources car Python et Flask sont plus lourds que Nginx.

Les ressources peuvent être surveillées avec :

```bash
docker stats
```

## Lancement du projet

Construire et démarrer tous les services :

```bash
docker compose up --build
```

Le projet est ensuite accessible sur :

```text
http://localhost:8080
```

L’API est accessible via le proxy sur :

```text
http://localhost:8080/api/
```

## Arrêt du projet

Pour arrêter et supprimer les conteneurs créés par Docker Compose :

```bash
docker compose down
```

Docker envoie un signal `SIGTERM` aux processus principaux pour s’arrêter proprement.