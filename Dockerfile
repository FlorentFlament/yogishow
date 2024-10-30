# Doc: https://hub.docker.com/_/nginx/
FROM nginx
COPY website /usr/share/nginx/html
