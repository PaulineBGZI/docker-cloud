# Benchmark de l'application

## Objectif

Le benchmark permet de tester les performances du catalogue de cookies et de vérifier la consommation des ressources des conteneurs Docker.

J'ai réalisé plusieurs tests sur les pages du site et sur l'API pour mesurer leur temps de réponse et le nombre de requêtes qu'ils peuvent traiter.

## Outils utilisés

### ApacheBench

J'ai choisi ApacheBench car c'est un outil simple qui permet de tester les performances d'un serveur web en envoyant plusieurs requêtes HTTP. Il permet de connaître le nombre de requêtes traitées par seconde, le temps de réponse moyen et le nombre de requêtes échouées. De plus, il n'y a pas besoin de modifier le code du projet pour l'utiliser.

### Docker Stats

J'ai utilisé la commande `docker stats` pour observer la consommation CPU et RAM des trois conteneurs pendant les tests. Cette commande est directement disponible avec Docker et permet de vérifier que les conteneurs respectent les limites de ressources définies dans le fichier `docker-compose.yml`.

## Tests réalisés

Les tests ont été effectués en local sur `http://localhost:8080`.

Les requêtes passent donc par le proxy Nginx avant d'être envoyées vers le frontend ou le backend.

J'ai testé trois routes :

- `/` : page d'accueil
- `/catalogue.html` : page catalogue
- `/api/` : API Flask

Pour chaque route, j'ai envoyé 1 000 requêtes avec 10 connexions simultanées.

La commande utilisée est la suivante, en adaptant l'URL selon la route :

```bash
ab -n 1000 -c 10 http://localhost:8080/
```

J'ai ensuite réalisé un test plus long sur l'API pour observer les performances et les ressources consommées pendant 30 secondes.

```bash
ab -t 30 -c 10 http://localhost:8080/api/
```

## Résultats

### Tests des trois routes

| Indicateur | Accueil | Catalogue | API |
|---|---:|---:|---:|
| Requêtes terminées | 1 000 | 1 000 | 1 000 |
| Requêtes échouées | 0 | 0 | 0 |
| Requêtes par seconde | 1 835,99 | 2 111,81 | 725,88 |
| Temps moyen | 5,45 ms | 4,74 ms | 13,78 ms |

Les trois routes ont répondu aux 1 000 requêtes sans erreur.
Les pages d'accueil et catalogue sont plus rapides que l'API.
Cela peut s'expliquer parce que les pages HTML passent par Nginx alors que l'API doit passer par Python et Flask pour renvoyer les données JSON.

### Test prolongé de l'API

| Indicateur | Résultat |
|---|---:|
| Durée | 30,07 secondes |
| Requêtes terminées | 16 096 |
| Requêtes échouées | 0 |
| Requêtes par seconde | 535,30 |
| Temps moyen | 18,68 ms |
| 95 % des requêtes traitées en | 84 ms ou moins |
| Temps maximal | 196 ms |

Pendant les 30 secondes du test, l'API a traité 16 096 requêtes sans erreur.
Le nombre de requêtes par seconde est plus faible que lors du premier test mais les deux tests n'ont pas la même durée.

### Consommation des ressources

J'ai utilisé `docker stats` pendant le test prolongé de l'API pour observer l'utilisation du CPU et de la RAM.

| Service | CPU observé | RAM utilisée | Limite RAM |
|---|---:|---:|---:|
| Front | 0,00 % | 10,22 MiB | 128 MiB |
| Back | 49,12 % | 23,69 MiB | 256 MiB |
| Proxy | 7,02 % | 6,57 MiB | 128 MiB |

Le backend est le service qui utilise le plus de CPU pendant le test car c'est lui qui traite les requêtes envoyées à l'API.

Le proxy consomme aussi du CPU puisqu'il reçoit les requêtes et les transmet au backend.
Le frontend ne travaille presque pas pendant ce test car les requêtes concernent uniquement l'API.
La consommation de mémoire des trois conteneurs reste bien inférieure aux limites définies dans Docker Compose.

## Conclusion

Les benchmarks montrent que le catalogue de cookies répond correctement aux tests réalisés.
Les trois routes ont traité toutes les requêtes sans erreur et les conteneurs restent sous leurs limites de mémoire.
L'API demande plus de ressources que les pages statiques, ce qui est normal puisqu'elle utilise Python et Flask.
