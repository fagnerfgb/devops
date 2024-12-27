#Autor: Fagner Geraldes Braga  
#Data de criação: 27/12/2024  
#Data de atualização: 27/12/2024  
#Versão: 0.01

[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](#)
[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](#)


## Desafio IMC - Apache

```docker
cd ~/devops/docker/desafios/imc
docker build -t fagnerfgb/imc:v1 -f Dockerfile .
docker tag fagnerfgb/imc:v1 fagnerfgb/imc:latest
```

### Enviar imagem ao DockerHub
```docker
docker login
docker push fagnerfgb/imc:v1
docker push fagnerfgb/imc:latest
```

### Executando container, testando, apagando container e apagando imagem
```docker
docker container run -d -p 8080:80 fagnerfgb/imc:v1

# Abrir o navegador e digitar IP:8080/imc

docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```