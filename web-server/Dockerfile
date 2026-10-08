# Nginx avec Alpine Linux comme image de base légère
FROM nginx:alpine

# Remplace la configuration Nginx par la configuration du reverse proxy
COPY nginx.conf /etc/nginx/nginx.conf

# Indique que le proxy écoute sur le port HTTP 80
EXPOSE 80
