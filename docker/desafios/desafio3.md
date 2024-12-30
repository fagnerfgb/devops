#Autor: Fagner Geraldes Braga  
#Data de criação: 17/12/2024  
#Data de atualização: 17/12/2024  
#Versão: 0.01

[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](#)
[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?logo=mongodb&logoColor=white)](#)


## Desafio 03 - Banco de Dados MongoDB

Pra finalizar essa etapa, crie o comando pra criar o banco de dados MongoDB usando os requisitos abaixo:

    O usuário root do banco deve ser mongo_usr
    A senha do usuário root deve ser mongo_pwd

Lembrando que a execução em container deve ser transparente pra quem está desenvolvendo. E que aqui você não precisa se preocupar com a perda dos dados do banco e nem nada disso, é apenas para desenvolvimento pontual.

Coloque aqui embaixo o comando que a equipe deve usar pra criar um banco de dados MongoDB com esses requisitos:

```docker
docker container run -d -p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=mongo_usr \
-e MONGO_INITDB_ROOT_PASSWORD=mongo_pwd \
mongo
```