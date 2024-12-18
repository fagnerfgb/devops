#Autor: Fagner Geraldes Braga  
#Data de criação: 13/12/2024  
#Data de atualização: 18/12/2024  
#Versão: 0.04

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

## Executando a aplicação dentro de um container
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
cd app
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
```docker


```