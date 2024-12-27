#Autor: Fagner Geraldes Braga  
#Data de criação: 13/12/2024  
#Data de atualização: 26/12/2024  
#Versão: 0.08

## namespace
```bash
unshare --pid --fork --mount-proc /bin/bash
```

```bash
ps -ef --forest
```

```bash
ps -aux
pwd
exit
```

## chroot
```bash
mkdir container
cd container
chroot .
ldd /bin/bash
```

```bash
apt update
apt install debootstrap -y
debootstrap jammy .
ls
ldd bin/bash
chroot .
ls /home
echo "teste" > teste.txt
exit
ls /root
ls root
```
```bash
chroot .
ps -aux
mount -t proc proc /proc
ps -aux
exit
```

## unshare e chroot
```bash
unshare --pid --fork --mount-proc chroot . /bin/bash
mount -t proc proc /proc
ps -aux
while true; do echo aula; done;
```

```bash
htop
```

## cgroup
```bash
ls /sys/fs/cgroup
echo "+cpu" >> /sys/fs/cgroup/cgroup.subtree_control
echo "+cpuset" >> /sys/fs/cgroup/cgroup.subtree_control
cd /sys/fs/cgroup
mkdir auladocker
cd aula docker
echo "+cpu" >> /sys/fs/cgroup/auladocker/cgroup.subtree_control
echo "+cpuset" >> /sys/fs/cgroup/auladocker/cgroup.subtree_control
# pegar pid do processo a ser gerenciado
echo "27528" >> /sys/fs/cgroup/auladocker/cgroup.procs
echo "0" >> /sys/fs/cgroup/auladocker/cpuset.cpus
echo "1" >> /sys/fs/cgroup/auladocker/cpuset.cpus
echo "500000 1000000" >> echo "0" >> /sys/fs/cgroup/auladocker/cpu.max
```
## LXC
```bash
apt update && apt install lxc lxc-templates -y
lxc-create -t ubuntu -n meucontainer
lxc-ls --fancy
lxc-start -n meucontainer
ps -ef --forest
lxc-attach -n meucontainer
ps -aux
```
## LXD
```bash
apt update && apt install lxd lxd-client -y
lxd init
lxc launch ubuntu:22.04 meucontainer
lxc list
lxc exec meucontainer -- bin/bash
ps -aux
lxc stop meucontainer
lxc delete meucontainer
```

## Docker Engine Install
https://docs.docker.com/engine/install/ubuntu/
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo groupadd docker

sudo usermod -aG docker $USER
```

## Primeiros passos
```docker
# executa container docker
docker container run hello-world

# lista os containers em execução
docker container ls

# lista todos os containers
docker container ls -a

# executa container e especifica um nome
docker container run --name meucontainer hello-world

# lista todos os containers
docker container ls -a

# remove container pelo id
docker container rm 1d4f5df815ba

# remove container pelo nome
docker container rm practical_noyce

# remove container pelos 4 primeiros algarismos do id
docker container rm 1dde

# executa container em modo interativo (-i) e ativa o terminal (-t)
docker container run -it ubuntu /bin/bash

# remove container pelo id
docker container rm 3603c3c73cbd

# executa container e quando o container é finalizado, ele é também excluído
docker container run --rm -it ubuntu /bin/bash
```

```docker
# executa container do nginx
# terminal fica preso porque o container executa de forma contínua
docker container run nginx

# executa o container e liberal o terminal
docker container run -d nginx

# coloca container específico em modo interativo
docker exec -it 4777a76cfd3a /bin/bash

# testando funcionamento do nginx dentro do próprio container
curl localhost
```
## Publicação de portas
```docker
# executa o container com a imagem do nginx 
# usando a porta 8080 do host e a porta 80 do container
docker container run -d -p 8080:80 nginx

lista os containers em execução
docker container ls

# parar a execução de um container
docker container stop 1f1ac2749a71

# inicia a execução de um container
docker container start 1f1ac2749a71

# remove container de forma forçada
docker container rm -f 1f1ac2749a71

# lista o id de todos os containers
docker container ls -qa

# remove todos os containers de uma vez de forma forçada
docker container rm -f $(docker container ls -qa)

lista os containers
docker container ls -a
```

## Variáveis de ambiente
```docker
# execução de container mysql
# desta forma dará erro porque falta os dados de configuração do mysql
docker container run -p 3306 -d mysql

# listar todos os containers
docker container ls -a

# verificar o log do container do mysql
docker logs a5ac6afa429e

# execução do container mysql com os dados para acesso ao mysql
docker container run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD="root1234" -e MYSQL_DATABASE=auladocker -e MYSQL_USER=userdocker -e MYSQL_PASSWORD=auladockerpwd mysql

# remove todos os containers de uma vez de forma forçada
docker container rm -f $(docker container ls -qa)
```
## Executando aplicação nodejs em servidor comum
```docker
sudo apt update
sudo apt upgrade -y
sudo apt install nodejs -y && sudo apt install npm -y
node -v
pwd
git clone https://github.com/KubeDev/conversao-temperatura.git
cd conversao-temperatura/src
npm install
npm audit fix
npm install
node server.js
```

### Executando a aplicação dentro de um container
```docker
# executa container com imagem ubuntu
# em modo interativo com terminal bash
# faz o bind da porta 8080 do servidor
# para a porta 8080 do container
 docker container run -it -p 8080:8080 ubuntu /bin/bash
```
### Instalando o nodejs no container
```docker
apt update
apt-get install -y curl
curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh
bash nodesource_setup.sh
apt-get install -y nodejs
node -v
```
### Copiando diretorio da aplicação do servidor para o container
```docker
cd conversao-temperatura/src/
docker container ls
docker container cp . c9a4d8016c6c:/app
```
### Instalando e executando a aplicação no container
```docker
cd /app
npm install
node server.js
```
## OverlayFS
```docker
cd /
sudo mkdir -p /overlay/primeira_camada
sudo mkdir -p /overlay/segunda_camada
sudo mkdir -p /overlay/work
sudo mkdir -p /overlay/merge
sudo apt install tree -y
tree /overlay/
echo "Arquivo teste na primeira camada" | sudo tee /overlay/primeira_camada/01_camada.txt
echo "Arquivo teste na segunda camada" | sudo tee /overlay/segunda_camada/02_camada.txt
tree /overlay/
sudo mount -t overlay -o lowerdir=/overlay/primeira_camada/,upperdir=/overlay/segunda_camada/,workdir=/overlay/work/ overlay /overlay/merge/
tree overlay/
echo "Arquivo merge" | sudo tee /overlay/merge/merge.txt
tree overlay/
```
## Copy-on-Write
```docker
echo "Alteração no arquivo" | sudo tee /overlay/merge/01_camada.txt
tree overlay/
```
## Docker Commit
### Executando a aplicação dentro de um container
```docker
# executa container com imagem ubuntu
# em modo interativo com terminal bash
# faz o bind da porta 8080 do servidor
# para a porta 8080 do container
 docker container run -it -p 8080:8080 ubuntu /bin/bash
```
### Instalando o nodejs no container
```docker
apt update
apt-get install -y curl
curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh
bash nodesource_setup.sh
apt-get install -y nodejs
node -v
```
### Copiando diretorio da aplicação do servidor para o container
```docker
cd conversao-temperatura/src/
docker container ls
docker container cp . a3cd2c7bc655:/app
```
### Instalando e executando a aplicação no container
```docker
cd /app
npm install
node server.js
```
### Criando o commit
```docker
docker container commit a3cd2c7bc655 conversao-temperatura
docker container rm -f $(docker container ls -qa)
```
### Executando a imagem criada
```docker
# Forma 1
docker container run -it -p 8080:8080 conversao-temperatura /bin/bash

# Forma 2
docker container run -d -p 8080:8080 conversao-temperatura node /app/server.js
docker container ls
```
### Entendendo melhor a imagem
```docker
docker image history ubuntu
docker image history conversao-temperatura
docker image inspect conversao-temperatura
docker image inspect conversao-temperatura > imagem.json
```

### Criando container e instalando curl
```docker
docker container run -it ubuntu /bin/bash
apt update
apt install curl -y
exit
```

### Criando Dockerfile01
```docker
FROM ubuntu
RUN apt update
RUN apt install curl -y
```

### Criando imagem a partir do Dockerfile e executando o container com a nova imagem
```docker
cd ~/devops/curl/
docker build -t ubuntu-curl -f Dockerfile01 .
docker image ls
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### Criando imagem a partir do Dockerfile sem usar o cache
```docker
docker build -t ubuntu-curl -f Dockerfile01 . --no-cache
```

### Adicionando vim ao Dockerfile
### Dockerfile02-vim
```docker
FROM ubuntu
RUN apt update
RUN apt install curl -y
RUN apt install vim -y
```
```docker
docker build -t ubuntu-curl -f Dockerfile02-vim .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### WORKDIR
### Dockerfile03-workdir
```docker
FROM ubuntu
RUN apt update && apt install curl -y
WORKDIR /app
```
```docker
docker build -t ubuntu-curl -f Dockerfile03-workdir .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### COPY
```docker
echo "Arquivo" > arquivo.txt
```
### Dockerfile04-copy
```docker
FROM ubuntu
RUN apt update && apt install curl -y
WORKDIR /app
COPY arquivo.txt .
```

```docker
docker build -t ubuntu-curl -f Dockerfile04-copy .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### ADD
### Dockerfile05-add
```docker
FROM ubuntu
RUN apt update && apt install curl -y
WORKDIR /app
ADD https://www.google.com pagina.html
```

```docker
docker build -t ubuntu-curl -f Dockerfile05-add .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

```docker
mkdir -p ~/devops/curl/teste
echo "Teste" > ~/devops/curl/teste/teste.txt
tar -zvcf teste.tar.gz teste/
rm -rf teste/
```
### Dockerfile06-add
```docker
FROM ubuntu
RUN apt update && apt install curl -y
WORKDIR /app
ADD teste.tar.gz ./
```

```docker
docker build -t ubuntu-curl -f Dockerfile06-add .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### LABEL
### Dockerfile07-label
```docker
FROM ubuntu
RUN apt update && apt install curl -y
LABEL contato="fagner.fgb@gmail.com"
WORKDIR /app
```
```docker
docker build -t ubuntu-curl -f Dockerfile07-label .
docker image inspect ubuntu-curl
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### ENV
### Dockerfile08-env
```docker
FROM ubuntu
RUN apt update && apt install curl -y
LABEL contato="fagner.fgb@gmail.com"
WORKDIR /app
ENV VALOR_DOCKER_ENV="Valor XPTO"
```
```docker
docker build -t ubuntu-curl -f Dockerfile08-env .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### VOLUME
```docker
FROM ubuntu
RUN apt update && apt install curl -y
LABEL contato="fagner.fgb@gmail.com"
VOLUME /app
```
```docker
docker build -t ubuntu-curl -f Dockerfile .
docker image inspect ubuntu-curl | grep -A 2 Volumes
```
### ARG
```docker
FROM ubuntu
RUN apt update && apt install curl -y
WORKDIR /app
ARG VAR_TEXTO="Texto XPTO"
RUN echo $VAR_TEXTO > arquivo.txt
```
```docker
docker build -t ubuntu-curl --build-arg VAR_TEXTO="Fagner Geraldes Braga" -f Dockerfile .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
```
### EXPOSE
```docker
FROM ubuntu
EXPOSE 80
RUN apt update && apt install nginx -y
WORKDIR /app
```
```docker
docker build -t ubuntu-nginx -f Dockerfile .
# -P pega uma porta disponível de forma aleatória
docker container run -it -P ubuntu-nginx /bin/bash
/usr/sbin/nginx -g "daemon off;"
exit
docker container rm -f $(docker container ls -qa)
```
### USER
```docker
FROM ubuntu
RUN useradd fagner
RUN apt update && apt install curl -y
WORKDIR /app
COPY --chown=fagner:fagner --chmod=777 ./aula/teste.txt .
USER fagner
```
```docker
docker build -t ubuntu-curl -f Dockerfile .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
```
### ENTRYPOINT
```docker
FROM ubuntu
RUN apt update && apt install curl -y
ENTRYPOINT [ "echo", "Hello World !" ]
```
```docker
docker build -t ubuntu-curl -f Dockerfile .
docker container run ubuntu-curl 
docker container rm -f $(docker container ls -qa)
```

```docker
FROM ubuntu
RUN apt update && apt install curl -y
ENTRYPOINT [ "echo", "Hello World !" ]
CMD [ "Combinado com o entrypoint" ]
```
```docker
docker build -t ubuntu-curl -f Dockerfile .
docker container run ubuntu-curl 
docker container run ubuntu-curl teste
docker container rm -f $(docker container ls -qa)
```
### entrypoint.sh
```bash
if [ -z $1 ]
then
    echo "Iniciando o container sem parametro"
else
    echo "Iniciando o container com o parametro $1"
fi
```
```docker
FROM ubuntu
RUN apt update && apt install curl -y
WORKDIR /app
COPY --chown=root:root --chmod=100 ./entrypoint.sh .
ENTRYPOINT [ "./entrypoint.sh" ]
```
```docker
docker build -t ubuntu-curl -f Dockerfile .
docker container run ubuntu-curl 
docker container run ubuntu-curl teste
docker container rm -f $(docker container ls -qa)
```

```docker
FROM ubuntu
RUN apt update && apt install curl -y
WORKDIR /app
COPY --chown=root:root --chmod=100 ./entrypoint.sh .
ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "XPTO" ]
```

```docker
docker build -t ubuntu-curl -f Dockerfile .
docker container run ubuntu-curl 
docker container run ubuntu-curl teste
docker container rm -f $(docker container ls -qa)
```

### PRINCIPAIS COMANDOS COM IMAGENS
```docker
docker commit
docker build
docker image ls
docker image rm
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### IMAGEM DA APLICAÇÃO COM DOCKERFILE
### Dockerfile01
```docker
FROM ubuntu
RUN apt update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh && \
    apt-get install -y nodejs
WORKDIR /app
COPY . .
RUN npm install
ENTRYPOINT [ "node", "server.js" ]
```
```docker
cd ~/devops/temperatura/src/
docker build -t conversao-temperatura -f Dockerfile01 .
docker image ls
docker container run -d -p 8080:8080 conversao-temperatura
docker container ls
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
## Docker Registry

### Alterando nome da imagem para ficar com nomenclatura correta
```docker
docker tag conversao-temperatura fagnerfgb/conversao-temperatura:v1
docker image ls
docker image rm -f $(docker image ls -qa)
docker image prune
```

### Criando imagem com a nomenclatura correta para envio ao DockerHub
```docker
cd ~/devops/temperatura/src/
# namespace/repositorio:tag
docker build -t fagnerfgb/conversao-temperatura:v1 -f Dockerfile01 .
docker tag fagnerfgb/conversao-temperatura:v1 fagnerfgb/conversao-temperatura:latest
```
### Enviar imagem ao DockerHub
```docker
docker login
docker push fagnerfgb/conversao-temperatura:v1
docker push fagnerfgb/conversao-temperatura:latest
docker image rm -f $(docker image ls -qa)
docker image prune
docker pull fagnerfgb/conversao-temperatura
```

### Boas práticas para construção de imagens
Um processo por container  
Usar imagens confiáveis  
Usar imagens tagueadas  
Linux Alpine é bem leve  
Uso inteligente das camadas
Dockerignore

### Alteração do Dockerfile
### Dockerfile-alpine01
```docker
FROM node:23.5.0-alpine3.20
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
ENTRYPOINT [ "node", "server.js" ]
```
```docker
docker build -t fagnerfgb/conversao-temperatura:v2 -f Dockerfile-alpine01 .
docker tag fagnerfgb/conversao-temperatura:v2 fagnerfgb/conversao-temperatura:latest
docker container run -d -p 8080:8080 fagnerfgb/conversao-temperatura:v2
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
## Multistage build
### Criando imagem simples do GoLang com a nossa aplicação

### Dockerfile.simples
```docker
FROM golang:1.23.4-alpine3.21
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .
CMD [ "./main" ]
```
```docker
git pull
cd devops/app
docker build -t fagnerfgb/app-multi-staging:simples -f Dockerfile.simples .
docker run -d -p 8080:8080 fagnerfgb/app-multi-staging:simples 
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### Dockerfile.multistage
```docker
FROM golang:1.23.4-alpine3.21 as build
WORKDIR /build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

FROM alpine:3.21.0 as app
WORKDIR /app
COPY --from=build /build/main .
CMD [ "./main" ]
```

```docker
docker build -t fagnerfgb/app-multistaging:multi -f Dockerfile.multistage .
docker container run -d -p 8080:8080 fagnerfgb/app-multistaging:multi
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
