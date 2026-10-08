# Utilise Nginx avec Alpine Linux comme image de base légère
FROM nginx:alpine

# Copie les fichiers du frontend dans le dossier servi par Nginx
COPY index.html /usr/share/nginx/html/index.html
COPY catalogue.html /usr/share/nginx/html/catalogue.html
COPY cookie.html /usr/share/nginx/html/cookie.html
COPY style.css /usr/share/nginx/html/style.css

# Copie les images du catalogue
COPY images /usr/share/nginx/html/images

# Indique que le serveur Nginx utilise le port HTTP 80
EXPOSE 80
