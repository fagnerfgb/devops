#Autor: Fagner Geraldes Braga  
#Data de criação: 17/12/2024  
#Data de atualização: 17/12/2024  
#Versão: 0.01

[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](#)
[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](#)


## Desafio 01 - Banco de Dados Postgresql

Você está dando os primeiros passos no uso de containers.
E a melhor forma de iniciar no mundo de containers é usar em ambiente de desenvolvimento.

Sua missão é ajudar a equipe de desenvolvimento a ter mais autonomia no desenvolvimento de projetos. E uma das reclamações da equipe é o setup local.

Crie um comando para criar um banco de dados PostgreSQL no ambiente do desenvolvedor de uma forma que cumpra os seguintes requisitos:

    O nome do banco de dados deve ser curso_docker
    O usuário de acesso ao banco deve ser docker_usr
    A senha do usuário deve ser docker_pwd

Lembrando que a execução em container deve ser transparente pra quem está desenvolvendo. E que aqui você não precisa se preocupar com a perda dos dados do banco e nem nada disso, é apenas para desenvolvimento pontual.

Coloque aqui embaixo o comando que a equipe deve usar pra criar um banco de dados PostgreSQL com esses requisitos.

```docker
docker container run -d -p 5432:5432 \ 
-e POSTGRES_PASSWORD="docker_pwd" \
-e POSTGRES_USER=docker_usr \
-e POSTGRES_DB=curso_docker \
postgres
```

### Usando o Dockerfile

[Desafio1](Dockerfile-desafio1)

```docker
docker build -t fagnerfgb/postgres:v1 -f Dockerfile-desafio1 .
docker container run -d -p 5432:5432 fagnerfgb/postgres:v1
```

```docker
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```docker