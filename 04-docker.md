#Autor: Fagner Geraldes Braga  
#Data de criação: 13/12/2024  
#Data de atualização: 31/12/2024  
#Versão: 0.10

### Primeiros passos com docker
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
docker container exec -it 4777a76cfd3a /bin/bash

# testando funcionamento do nginx dentro do próprio container
curl localhost
```
### Publicação de portas
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

### Variáveis de ambiente
```docker
# execução de container mysql
# desta forma dará erro porque falta os dados de configuração do mysql
docker container run -p 3306 -d mysql

# listar todos os containers
docker container ls -a

# verificar o log do container do mysql
docker logs a5ac6afa429e

# execução do container mysql com os dados para acesso ao mysql
docker container run -d -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD="root1234" \
-e MYSQL_DATABASE=auladocker \
-e MYSQL_USER=userdocker \
-e MYSQL_PASSWORD=auladockerpwd \
mysql

# remove todos os containers de uma vez de forma forçada
docker container rm -f $(docker container ls -qa)
```
### Executando aplicação nodejs em servidor comum
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
### OverlayFS
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
sudo mount -t overlay -o lowerdir=/overlay/primeira_camada/,upperdir=/overlay/segunda_camada/,workdir=/overlay/work/ \
overlay /overlay/merge/
tree overlay/
echo "Arquivo merge" | sudo tee /overlay/merge/merge.txt
tree overlay/
```
### Copy-on-Write
```docker
echo "Alteração no arquivo" | sudo tee /overlay/merge/01_camada.txt
tree overlay/
```
### Docker Commit
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
## Todos os arquivos Dockerfile desta parte estão dentro da pasta curl
### Dockerfile01
[Dockerfile01](curl/Dockerfile01)

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

[Dockerfile02-vim](curl/Dockerfile02-vim)

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

[Dockerfile03-workdir](curl/Dockerfile03-workdir)

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
[Dockerfile04-copy](curl/Dockerfile04-copy)

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
[Dockerfile05-add](curl/Dockerfile05-add)

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
[Dockerfile06-add](curl/Dockerfile06-add)


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
[Dockerfile07-label](curl/Dockerfile07-label)

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
[Dockerfile08-env](curl/Dockerfile08-env)

```docker
docker build -t ubuntu-curl -f Dockerfile08-env .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### VOLUME
### Dockerfile09-vol
[Dockerfile09-vol](curl/Dockerfile09-vol)

```docker
docker build -t ubuntu-curl -f Dockerfile09-vol .
docker image inspect ubuntu-curl | grep -A 2 Volumes
```
### ARG
### Dockerfile10-arg
[Dockerfile10-arg](curl/Dockerfile10-arg)

```docker
docker build -t ubuntu-curl --build-arg VAR_TEXTO="Fagner Geraldes Braga" -f Dockerfile10-arg .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### EXPOSE
### Dockerfile11-exp
[Dockerfile11-exp](curl/Dockerfile11-exp)

```docker
docker build -t ubuntu-nginx -f Dockerfile11-exp .
# -P pega uma porta disponível de forma aleatória
docker container run -it -P ubuntu-nginx /bin/bash
/usr/sbin/nginx -g "daemon off;"
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### USER
### Dockerfile12-usr
[Dockerfile12-usr](curl/Dockerfile12-usr)

```docker
docker build -t ubuntu-curl -f Dockerfile12-usr .
docker container run -it ubuntu-curl /bin/bash
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### ENTRYPOINT
### Dockerfile13-epoint
[Dockerfile13-epoint](curl/Dockerfile13-epoint)

```docker
docker build -t ubuntu-curl -f Dockerfile13-epoint .
docker container run ubuntu-curl 
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### ENTRYPOINT COMBINADO COM CMD
### Dockerfile14-epointcmd
[Dockerfile14-epointcmd](curl/Dockerfile14-epointcmd)

```docker
docker build -t ubuntu-curl -f Dockerfile14-epointcmd .
docker container run ubuntu-curl 
docker container run ubuntu-curl teste
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### entrypoint.sh
[entrypoint.sh](curl/entrypoint.sh)

### SCRIPT ENTRYPOINT
### Dockerfile15-sc-epoint
[Dockerfile15-sc-epoint](curl/Dockerfile15-sc-epoint)

```docker
docker build -t ubuntu-curl -f Dockerfile15-sc-epoint .
docker container run ubuntu-curl 
docker container run ubuntu-curl teste
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### SCRIPT ENTRYPOINT
### Dockerfile16-mix
[Dockerfile16-mix](curl/Dockerfile16-mix)

```docker
docker build -t ubuntu-curl -f Dockerfile16-mix .
docker container run ubuntu-curl 
docker container run ubuntu-curl teste
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
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
## Todos os arquivos Dockerfile desta parte estão dentro da pasta temperatura/src/
### IMAGEM DA APLICAÇÃO COM DOCKERFILE
### Dockerfile01
[Dockerfile01](temperatura/src/Dockerfile01)

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
[Dockerfile-alpine01](temperatura/src/Dockerfile-alpine01)

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
## Todos os arquivos Dockerfile desta parte estão dentro da pasta golang

### Dockerfile.simples
[Dockerfile.simples](golang/Dockerfile.simples)

```docker
cd ~/devops
git pull
cd ~/devops/golang
docker build -t fagnerfgb/app-multi-staging:simples -f Dockerfile.simples .
docker run -d -p 8080:8080 fagnerfgb/app-multi-staging:simples 
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```
### Dockerfile.multistage
[Dockerfile.multistage](golang/Dockerfile.multistage)

```docker
docker build -t fagnerfgb/app-multistaging:multi -f Dockerfile.multistage .
docker container run -d -p 8080:8080 fagnerfgb/app-multistaging:multi
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### Construindo a imagem intermediária "build"
### Dockerfile.multistage
[Dockerfile.multistage](golang/Dockerfile.multistage)

```docker
docker build -t fagnerfgb/app-multistaging:multi -f Dockerfile.multistage --target=build .
docker container run -d -p 8080:8080 fagnerfgb/app-multistaging:multi
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### Copiar arquivos de outras imagens
### Dockerfile.pacote-bin
[Dockerfile.pacote-bin](golang/Dockerfile.pacote-bin)

```docker
docker container run -it fabricioveronez/pacote-bin:v1 /bin/sh
ls
exit
```
```docker
docker build -t fagnerfgb/app-multistaging-copia:multistaging -f Dockerfile.pacote-bin .
docker container run -d -p 8080:8080 fagnerfgb/app-multistaging-copia:multistaging
docker container ls
docker container exec -it 4156db95e96f /bin/sh
ls
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### Usando imagem intermediária como base para outra imagem
### Dockerfile.intermediaria
[Dockerfile.intermediaria](golang/Dockerfile.intermediaria)

```docker
docker build -t fagnerfgb/app-multistaging-intermediaria:intermediaria -f Dockerfile.intermediaria .
docker container run -d -p 8080:8080 fagnerfgb/app-multistaging-intermediaria:intermediaria
docker container ls
docker container exec -it c8ab0638f446 /bin/sh
ls
exit
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

## Volumes
### Bind Mount
Mapeia um diretório sistema de arquivo do host com um diretório do container

```docker
mkdir aula_volume
docker container run -it --mount type=bind,source="$(pwd)/aula_volume",target=/app ubuntu /bin/bash
echo "Teste" > /app/teste.txt
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

[Dockerfile-bind](aula_volume/Dockerfile-bind)
```docker
docker build -t fagnerfgb/volume-bind:v1 -f aula_volume/Dockerfile-bind .
docker container run -it --mount type=bind,source="$(pwd)/aula_volume",target=/app fagnerfgb/volume-bind:v1 /bin/bash
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### Bind de diretório
```docker
docker container run -d -p 8080:80 -v $(pwd)/aula_volume/html:/usr/share/nginx/html nginx
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### Bind de arquivo
```docker
docker container run -d -p 8080:80 -v $(pwd)/aula_volume/html/index.html:/usr/share/nginx/html/index.html nginx
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

### Docker Volume
Gerenciado pelo docker

#### Comandos básicos
```docker
docker volume create aula_volume
docker volume ls
docker volume inspect aula_volume
docker volume rm aula_volume
```
```docker
docker volume create aula_volume
docker container run -it --mount type=volume,source=aula_volume,target=/app ubuntu /bin/bash
docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
```

```docker
docker volume ls
docker volume inspect aula_volume
docker volume prune
```

[Dockerfile-volume](aula_volume/Dockerfile-volume)


```docker
docker build -t fagnerfgb/volume:v1 -f aula_volume/Dockerfile-volume .

# como no dockerfile foi dada a instrução para criar um 
# volume e no comando abaixo não foi referenciado, o docker
# cria um volume com um id aleatório
docker container run -it fagnerfgb/volume:v1 /bin/bash
exit
docker volume ls

docker container run -it -v aula_volume:/app fagnerfgb/volume:v1 /bin/bash

docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
docker volume prune
```

### Backup de um docker volume
```docker
# como no dockerfile foi dada a instrução para criar um 
# volume e no comando abaixo não foi referenciado, o docker
# cria um volume com um id aleatório
docker build -t fagnerfgb/volume:v1 -f aula_volume/Dockerfile-volume .
docker container run -it fagnerfgb/volume:v1 /bin/bash
```

```docker
echo "Teste" > teste.txt
echo "Exemplo" > exemplo.txt
exit
```

```docker
docker container ls -a

# --volumes-from id --> pega todos os volumes do container do passo anterior 
# e coloca dentro do novo container criado
docker container run --volumes-from 823a0c12800b --rm -v $(pwd):/backup fagnerfgb/volume:v1 tar cvf /backup/bkp_vol.tar /app
# cria volume com o nome "novo_volume"
docker volume create novo_volume

# restaura o backup no novo container, colocando os dados no volume "novo_volume"
docker container run -v $(pwd):/backup -v novo_volume:/app fagnerfgb/volume:v1 tar xvf /backup/bkp_vol.tar

docker container rm -f $(docker container ls -qa)
docker image rm -f $(docker image ls -qa)
docker image prune
docker volume prune
```

### Exemplo com um docker volume (Bind)
```docker
mkdir db_vol
docker container run -d -p 5432:5432 -e POSTGRES_PASSWORD="docker_pwd" --mount type=bind,source="$(pwd)/db_vol",target=/var/lib/postgresql/data postgres
docker container rm -f $(docker container ls -qa)
```

### Exemplo com um docker volume (Volume)
```docker
docker container run -d -p 5432:5432 -e POSTGRES_PASSWORD="docker_pwd" --mount type=volume,source=container_postgre_vol,target=/var/lib/postgresql/data postgres
docker container rm -f $(docker container ls -qa)
```


```docker
docker image rm -f $(docker image ls -qa)
docker image prune
docker volume prune
```

### Exemplo com tmpfs
```docker
docker container run -it --mount type=tmpfs,target=/app ubuntu:22.04 /bin/bash
```

### Postgres
```docker
docker container run -d -p 5432:5432 -e POSTGRES_PASSWORD="pwdkubenews" -e POSTGRES_USER=kubenews -e POSTGRES_DB=kubenews -v kubenews_vol:/var/lib/postgresql/data postgres:14:10
docker container rm -f $(docker container ls -qa)
```


### Executando aplicação nodejs em servidor comum
```docker
sudo apt update
sudo apt install nodejs -y && sudo apt install npm -y
node -v
cd ~/devops/kube-news/src/
npm install
npm audit fix
node server.js
```
