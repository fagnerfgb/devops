#Autor: Fagner Geraldes Braga  
#Data de criação: 27/12/2024  
#Data de atualização: 27/12/2024  
#Versão: 0.01

[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](#)

## Desafio Astrojupiter

```docker
cd ~/devops/docker/desafios/astrojupiter
docker build -t fagnerfgb/astrojupiter:v1 -f Dockerfile .
docker tag fagnerfgb/astrojupiter:v1 fagnerfgb/astrojupiter:latest
```

### Enviar imagem ao DockerHub
```docker
docker login
docker push fagnerfgb/astrojupiter:v1
docker push fagnerfgb/astrojupiter:latest
```

### Executando container, testando, apagando container e apagando imagem
```docker
docker container run -d -p 8080:80 fagnerfgb/astrojupiter:v1

# Abrir o navegador e digitar IP:8080/astrojupiter/index.html

docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
# docker run --rm --entrypoint=cat nginx:1.26.2-alpine3.20 /etc/nginx/conf.d/default.conf > ./default.conf
```


