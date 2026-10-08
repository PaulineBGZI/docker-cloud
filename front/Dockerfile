# Nginx avec Alpine Linux comme image de base légère
FROM nginx:alpine

# Copie les fichiers du frontend dans le dossier servi par Nginx
COPY index.html /usr/share/nginx/html/index.html
COPY style.css /usr/share/nginx/html/style.css

# Indique que le serveur Nginx utilise le port HTTP 80
EXPOSE 80
