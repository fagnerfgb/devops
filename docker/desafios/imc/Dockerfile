#Autor: Fagner Geraldes Braga
#Data de criação: 30/12/2024
#Data de atualização: 30/12/2024
#Versão: 0.01

#FROM (Create a new build stage from a base image)
FROM httpd:2.4.62-alpine3.21

#EXPOSE (Describe which ports your application is listening on)
EXPOSE 80

#LABEL (Add metadata to an image)
LABEL author="Fagner Geraldes Braga"
LABEL contact="fagner.fgb@gmail.com"
LABEL description="Linux Alpine with Web server NGINX"
LABEL source="https://github.com/fagnerfgb/devops"
LABEL documentation="https://github.com/fagnerfgb/devops/blob/master/docker/desafios/desafio-astrojupiter.md"

#COPY: (Copy files and directories)
COPY . /usr/local/apache2/htdocs/imc


