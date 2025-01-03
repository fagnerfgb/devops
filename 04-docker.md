#Autor: Fagner Geraldes Braga  
#Data de criação: 13/12/2024  
#Data de atualização: 03/01/2025  
#Versão: 0.12

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
docker container run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD="root1234" -e MYSQL_DATABASE=auladocker -e MYSQL_USER=userdocker -e MYSQL_PASSWORD=auladockerpwd mysql

# remove todos os containers de uma vez de forma forçada
docker container rm -f $(docker container ls -qa)
```
### Executando aplicação nodejs em servidor comum
```docker
# Atualiza a lista de pacotes disponíveis nos repositórios configurados
sudo apt update

# Instala as versões mais recentes dos pacotes instalados no sistema, aplicando atualizações
sudo apt upgrade -y

# Instala o Node.js e o npm (gerenciador de pacotes do Node.js)
sudo apt install nodejs -y && sudo apt install npm -y

# Verifica a versão instalada do Node.js
node -v

# Mostra o diretório atual (print working directory)
pwd

# Clona o repositório do projeto "conversao-temperatura" do GitHub para o diretório atual
git clone https://github.com/KubeDev/conversao-temperatura.git

# Navega para o diretório do projeto clonado
cd conversao-temperatura/src

# Instala as dependências do projeto definidas no arquivo package.json
npm install

# Tenta corrigir vulnerabilidades ou problemas de segurança nas dependências do projeto
npm audit fix

# Reinstala as dependências do projeto (opcional, se necessário após o audit fix)
npm install

# Inicia o servidor do projeto utilizando o arquivo server.js
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
# Atualiza a lista de pacotes disponíveis nos repositórios configurados
apt update

# Instala o utilitário curl para transferências de dados via comandos HTTP, HTTPS, FTP, etc.
apt-get install -y curl

# Faz o download do script de configuração do repositório Nodesource para instalar a versão 23.x do Node.js
curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh

# Executa o script baixado para configurar o repositório do Node.js no sistema
bash nodesource_setup.sh

# Instala o Node.js a partir do repositório configurado pelo script
apt-get install -y nodejs

# Exibe a versão instalada do Node.js para verificar a instalação
node -v
```
### Copiando diretorio da aplicação do servidor para o container
```docker
# Navega para o diretório "src" dentro do projeto "conversao-temperatura"
cd conversao-temperatura/src/

# Lista todos os contêineres Docker em execução no momento
docker container ls

# Copia o conteúdo do diretório atual (.) para o diretório "/app" dentro do contêiner Docker identificado pelo ID "c9a4d8016c6c"
docker container cp . c9a4d8016c6c:/app
```
### Instalando e executando a aplicação no container
```docker
# Navega para o diretório "/app" dentro do sistema de arquivos ou contêiner
cd /app

# Instala as dependências do projeto definidas no arquivo package.json
npm install

# Inicia o servidor do projeto utilizando o arquivo server.js
node server.js
```
### OverlayFS
```docker
# Navega para o diretório raiz do sistema de arquivos
cd /

# Cria o diretório "/overlay/primeira_camada" e quaisquer diretórios necessários no caminho
sudo mkdir -p /overlay/primeira_camada

# Cria o diretório "/overlay/segunda_camada" e quaisquer diretórios necessários no caminho
sudo mkdir -p /overlay/segunda_camada

# Cria o diretório "/overlay/work" para ser usado como área de trabalho pelo sistema de arquivos Overlay
sudo mkdir -p /overlay/work

# Cria o diretório "/overlay/merge" onde será montado o sistema de arquivos Overlay
sudo mkdir -p /overlay/merge

# Instala o comando "tree" para visualizar a estrutura de diretórios de forma hierárquica
sudo apt install tree -y

# Exibe a estrutura atual do diretório "/overlay"
tree /overlay/

# Cria um arquivo de texto na "primeira camada" com o conteúdo "Arquivo teste na primeira camada"
echo "Arquivo teste na primeira camada" | sudo tee /overlay/primeira_camada/01_camada.txt

# Cria um arquivo de texto na "segunda camada" com o conteúdo "Arquivo teste na segunda camada"
echo "Arquivo teste na segunda camada" | sudo tee /overlay/segunda_camada/02_camada.txt

# Exibe novamente a estrutura do diretório "/overlay" para mostrar os novos arquivos
tree /overlay/

# Monta o sistema de arquivos Overlay com:
# - "lowerdir" apontando para a primeira camada
# - "upperdir" apontando para a segunda camada
# - "workdir" como diretório de trabalho
# - O resultado sendo mesclado no diretório "merge"
sudo mount -t overlay -o lowerdir=/overlay/primeira_camada/,upperdir=/overlay/segunda_camada/,workdir=/overlay/work/ \
overlay /overlay/merge/

# Exibe a estrutura de "/overlay" após a montagem do sistema de arquivos Overlay
tree overlay/

# Cria um arquivo de texto no diretório "merge" (camada mesclada) com o conteúdo "Arquivo merge"
echo "Arquivo merge" | sudo tee /overlay/merge/merge.txt

# Exibe novamente a estrutura do diretório "/overlay" para mostrar o novo arquivo criado no "merge"
tree overlay/
```
### Copy-on-Write
```docker
# Sobrescreve o conteúdo do arquivo "01_camada.txt" no diretório "/overlay/merge" (camada mesclada) 
# com o texto "Alteração no arquivo". Essa modificação será feita na camada superior (segunda camada).
echo "Alteração no arquivo" | sudo tee /overlay/merge/01_camada.txt

# Exibe a estrutura atual do diretório "/overlay" após a alteração
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
# Atualiza a lista de pacotes disponíveis nos repositórios configurados
apt update

# Instala o utilitário curl, usado para transferências de dados via HTTP, HTTPS, FTP, etc.
apt-get install -y curl

# Baixa o script de configuração do repositório Nodesource para a instalação da versão 23.x do Node.js
curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh

# Executa o script baixado para adicionar o repositório do Node.js ao sistema
bash nodesource_setup.sh

# Instala o Node.js a partir do repositório configurado pelo script
apt-get install -y nodejs

# Exibe a versão instalada do Node.js para verificar a instalação
node -v
```
### Copiando diretorio da aplicação do servidor para o container
```docker
# Navega para o diretório "src" dentro do projeto "conversao-temperatura"
cd conversao-temperatura/src/

# Lista todos os contêineres Docker em execução no momento, mostrando informações como ID, nome, e estado
docker container ls

# Copia todo o conteúdo do diretório atual (.) para o diretório "/app" no contêiner Docker com o ID "a3cd2c7bc655"
docker container cp . a3cd2c7bc655:/app
```
### Instalando e executando a aplicação no container
```docker
# Navega para o diretório "/app" no sistema de arquivos ou dentro do contêiner
cd /app

# Instala todas as dependências do projeto especificadas no arquivo package.json
npm install

# Inicia o servidor do projeto usando o arquivo server.js
node server.js
```
### Criando o commit
```docker
# Cria uma imagem Docker a partir do contêiner "a3cd2c7bc655" e nomeia a imagem como "conversao-temperatura"
docker container commit a3cd2c7bc655 conversao-temperatura

# Remove todos os contêineres Docker, forçando a remoção de contêineres em execução ou parados
# O comando $(docker container ls -qa) lista os IDs de todos os contêineres (ativos ou não)
docker container rm -f $(docker container ls -qa)

```
### Executando a imagem criada
```docker
# Forma 1
# Executa o contêiner "conversao-temperatura" em modo interativo (-it), 
# mapeando a porta 8080 do contêiner para a porta 8080 do host, 
# e abre o terminal interativo do contêiner com o comando /bin/bash
docker container run -it -p 8080:8080 conversao-temperatura /bin/bash


# Forma 2
# Executa o contêiner "conversao-temperatura" em segundo plano (-d),
# mapeando a porta 8080 do contêiner para a porta 8080 do host,
# e executa o comando "node /app/server.js" dentro do contêiner para iniciar o servidor
docker container run -d -p 8080:8080 conversao-temperatura node /app/server.js

# Lista todos os contêineres em execução no momento, mostrando informações como ID, nome e estado
docker container ls
```
### Entendendo melhor a imagem
```docker
# Exibe o histórico de camadas da imagem "ubuntu", mostrando informações sobre cada camada, como data, comandos e tamanho
docker image history ubuntu

# Exibe o histórico de camadas da imagem "conversao-temperatura"
docker image history conversao-temperatura

# Exibe detalhes completos sobre a imagem "conversao-temperatura", incluindo metadados como tamanho, camadas e configurações
docker image inspect conversao-temperatura

# Salva os detalhes completos da imagem "conversao-temperatura" em um arquivo JSON chamado "imagem.json"
docker image inspect conversao-temperatura > imagem.json
```
### Criando container e instalando curl
```docker
# Executa um contêiner Ubuntu em modo interativo (-it) e abre o terminal bash dentro do contêiner
docker container run -it ubuntu /bin/bash

# Atualiza a lista de pacotes disponíveis nos repositórios configurados dentro do contêiner
apt update

# Instala o utilitário curl no contêiner para transferências de dados via HTTP, HTTPS, FTP, etc.
apt install curl -y

# Sai do terminal interativo do contêiner, fechando a sessão
exit
```
## Todos os arquivos Dockerfile desta parte estão dentro da pasta curl
### Dockerfile01
[Dockerfile01](curl/Dockerfile01)

### Criando imagem a partir do Dockerfile e executando o container com a nova imagem
```docker
# Navega para o diretório "~/devops/curl/", onde o Dockerfile está localizado
cd ~/devops/curl/

# Constrói uma imagem Docker chamada "ubuntu-curl" a partir do Dockerfile "Dockerfile01" no diretório atual
docker build -t ubuntu-curl -f Dockerfile01 .

# Lista todas as imagens Docker disponíveis localmente
docker image ls

# Executa o contêiner "ubuntu-curl" em modo interativo (-it) e abre o terminal bash dentro do contêiner
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal interativo do contêiner
exit

# Remove todos os contêineres Docker, forçando a remoção de contêineres em execução ou parados
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens
docker image rm -f $(docker image ls -qa)

# Remove imagens não utilizadas ou órfãs que não estão mais associadas a contêineres
docker image prune
```

### Criando imagem a partir do Dockerfile sem usar o cache
```docker
# Constrói uma imagem Docker chamada "ubuntu-curl" a partir do Dockerfile "Dockerfile01" no diretório atual,
# utilizando a opção "--no-cache" para garantir que o build seja feito sem usar o cache de camadas anteriores
docker build -t ubuntu-curl -f Dockerfile01 . --no-cache
```

### Adicionando vim ao Dockerfile
### Dockerfile02-vim

[Dockerfile02-vim](curl/Dockerfile02-vim)

```docker
# Constrói uma imagem Docker chamada "ubuntu-curl" a partir do Dockerfile "Dockerfile02-vim" no diretório atual
docker build -t ubuntu-curl -f Dockerfile02-vim .

# Executa o contêiner "ubuntu-curl" em modo interativo (-it) e abre o terminal bash dentro do contêiner
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal interativo do contêiner
exit

# Remove todos os contêineres Docker, forçando a remoção de contêineres em execução ou parados
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens
docker image rm -f $(docker image ls -qa)

# Remove imagens não utilizadas ou órfãs que não estão mais associadas a contêineres
docker image prune
```
### WORKDIR
### Dockerfile03-workdir

[Dockerfile03-workdir](curl/Dockerfile03-workdir)

```docker
# Constrói uma imagem Docker chamada "ubuntu-curl" a partir do Dockerfile "Dockerfile03-workdir" no diretório atual
docker build -t ubuntu-curl -f Dockerfile03-workdir .

# Executa o contêiner "ubuntu-curl" em modo interativo (-it) e abre o terminal bash dentro do contêiner
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal interativo do contêiner
exit

# Remove todos os contêineres Docker, forçando a remoção de contêineres em execução ou parados
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens
docker image rm -f $(docker image ls -qa)

# Remove imagens não utilizadas ou órfãs que não estão mais associadas a contêineres
docker image prune
```

### COPY
```docker
# Cria um arquivo chamado "arquivo.txt" (ou sobrescreve se já existir) e escreve o texto "Arquivo" nele
echo "Arquivo" > arquivo.txt

```
### Dockerfile04-copy
[Dockerfile04-copy](curl/Dockerfile04-copy)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile04-copy no diretório atual.
# A opção "-f" especifica o Dockerfile a ser usado para a construção da imagem.
docker build -t ubuntu-curl -f Dockerfile04-copy .

# Executa um contêiner da imagem "ubuntu-curl" em modo interativo (-it) e acessa o terminal bash dentro do contêiner
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal ou contêiner atual
exit

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```

### ADD
### Dockerfile05-add
[Dockerfile05-add](curl/Dockerfile05-add)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile05-add no diretório atual.
# A opção "-f" especifica o Dockerfile a ser usado para a construção da imagem.
docker build -t ubuntu-curl -f Dockerfile05-add .

# Executa um contêiner da imagem "ubuntu-curl" em modo interativo (-it) e acessa o terminal bash dentro do contêiner
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal ou contêiner atual
exit

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```

```docker
# Cria o diretório ~/devops/curl/teste, incluindo os diretórios pai se necessário (-p)
mkdir -p ~/devops/curl/teste

# Cria um arquivo chamado teste.txt dentro do diretório ~/devops/curl/teste e adiciona o texto "Teste" nele
echo "Teste" > ~/devops/curl/teste/teste.txt

# Cria um arquivo compactado no formato .tar.gz a partir do diretório teste
# O comando -z aplica compressão gzip, -v é para modo verbose (exibe o que está sendo feito), e -c cria o arquivo tar
tar -zvcf teste.tar.gz teste/

# Remove recursivamente o diretório "teste" e todo seu conteúdo
rm -rf teste/
```
### Dockerfile06-add
[Dockerfile06-add](curl/Dockerfile06-add)


```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile06-add no diretório atual.
# A opção "-f" especifica o Dockerfile a ser usado para a construção da imagem.
docker build -t ubuntu-curl -f Dockerfile06-add .

# Executa um contêiner da imagem "ubuntu-curl" em modo interativo (-it) e acessa o terminal bash dentro do contêiner
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal ou contêiner atual
exit

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```

### LABEL
### Dockerfile07-label
[Dockerfile07-label](curl/Dockerfile07-label)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile07-label no diretório atual.
# A opção "-f" especifica o Dockerfile a ser usado para a construção da imagem.
docker build -t ubuntu-curl -f Dockerfile07-label .

# Inspeciona a imagem "ubuntu-curl" para exibir detalhes como etiquetas (labels), camadas e outras informações.
docker image inspect ubuntu-curl

# Executa um contêiner da imagem "ubuntu-curl" em modo interativo (-it) e acessa o terminal bash dentro do contêiner
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal ou contêiner atual
exit

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```

### ENV
### Dockerfile08-env
[Dockerfile08-env](curl/Dockerfile08-env)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile08-env no diretório atual.
# A opção "-f" especifica o Dockerfile a ser usado para a construção da imagem.
docker build -t ubuntu-curl -f Dockerfile08-env .

# Executa um contêiner da imagem "ubuntu-curl" em modo interativo (-it) e acessa o terminal bash dentro do contêiner
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal ou contêiner atual
exit

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```
### VOLUME
### Dockerfile09-vol
[Dockerfile09-vol](curl/Dockerfile09-vol)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile09-vol no diretório atual.
# A opção "-f" especifica o Dockerfile a ser usado para a construção da imagem.
docker build -t ubuntu-curl -f Dockerfile09-vol .

# Inspeciona a imagem "ubuntu-curl" e filtra a seção "Volumes" usando o comando grep
# O comando "grep -A 2 Volumes" exibe a linha "Volumes" e as duas linhas seguintes, permitindo ver as informações relacionadas a volumes.
docker image inspect ubuntu-curl | grep -A 2 Volumes
```
### ARG
### Dockerfile10-arg
[Dockerfile10-arg](curl/Dockerfile10-arg)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile10-arg no diretório atual.
# A opção "--build-arg VAR_TEXTO='Fagner Geraldes Braga'" passa o valor "Fagner Geraldes Braga" para a variável de construção VAR_TEXTO.
# O Dockerfile pode usar essa variável durante a construção da imagem.
docker build -t ubuntu-curl --build-arg VAR_TEXTO="Fagner Geraldes Braga" -f Dockerfile10-arg .

# Executa um contêiner da imagem "ubuntu-curl" em modo interativo (-it) e acessa o terminal bash dentro do contêiner.
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal ou contêiner atual
exit

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```
### EXPOSE
### Dockerfile11-exp
[Dockerfile11-exp](curl/Dockerfile11-exp)

```docker
# Constrói a imagem Docker chamada "ubuntu-nginx" a partir do Dockerfile11-exp no diretório atual.
# O Dockerfile pode configurar a instalação do Nginx ou outras personalizações.
docker build -t ubuntu-nginx -f Dockerfile11-exp .

# Executa um contêiner da imagem "ubuntu-nginx" em modo interativo (-it), com a opção -P que mapeia uma porta aleatória do contêiner para uma porta disponível no host.
# A opção "/bin/bash" abre o terminal bash dentro do contêiner para interações.
docker container run -it -P ubuntu-nginx /bin/bash

# Inicia o Nginx no contêiner, fazendo com que o processo de Nginx rode em primeiro plano (sem daemonização)
# O comando "-g 'daemon off;'" garante que o Nginx não seja executado em segundo plano e permaneça ativo.
# Isso é necessário para contêineres Docker, já que o contêiner terminaria se o processo principal (PID 1) terminasse.
# O Nginx, portanto, continua em execução no contêiner.
usr/sbin/nginx -g "daemon off;"

# Sai do terminal ou contêiner atual
exit

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```
### USER
### Dockerfile12-usr
[Dockerfile12-usr](curl/Dockerfile12-usr)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile12-usr no diretório atual.
# O Dockerfile pode configurar o contêiner para instalar ou configurar pacotes, incluindo o curl, ou outros recursos.
docker build -t ubuntu-curl -f Dockerfile12-usr .

# Executa um contêiner da imagem "ubuntu-curl" em modo interativo (-it), abrindo o terminal bash dentro do contêiner.
docker container run -it ubuntu-curl /bin/bash

# Sai do terminal ou contêiner atual
exit

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```
### ENTRYPOINT
### Dockerfile13-epoint
[Dockerfile13-epoint](curl/Dockerfile13-epoint)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile13-epoint no diretório atual.
# O Dockerfile pode configurar o contêiner com comandos adicionais, como a instalação de pacotes ou a configuração de arquivos.
docker build -t ubuntu-curl -f Dockerfile13-epoint .

# Executa um contêiner a partir da imagem "ubuntu-curl". 
# O contêiner será executado em segundo plano ou até o término do processo configurado no Dockerfile.
docker container run ubuntu-curl 

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```

### ENTRYPOINT COMBINADO COM CMD
### Dockerfile14-epointcmd
[Dockerfile14-epointcmd](curl/Dockerfile14-epointcmd)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile14-epointcmd no diretório atual.
# O Dockerfile pode definir comandos específicos ou configurações que serão executados quando o contêiner for iniciado.
docker build -t ubuntu-curl -f Dockerfile14-epointcmd .

# Executa um contêiner a partir da imagem "ubuntu-curl" usando o comando padrão definido no Dockerfile.
# O contêiner será iniciado com o comando configurado no Dockerfile.
docker container run ubuntu-curl 

# Executa outro contêiner a partir da imagem "ubuntu-curl" com um argumento adicional "teste" que pode ser interpretado pelo comando de entrada.
# Isso pode substituir o comando padrão ou ser usado como argumento para o processo do contêiner.
docker container run ubuntu-curl teste

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço.
docker image prune
```
### entrypoint.sh
[entrypoint.sh](curl/entrypoint.sh)

### SCRIPT ENTRYPOINT
### Dockerfile15-sc-epoint
[Dockerfile15-sc-epoint](curl/Dockerfile15-sc-epoint)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile15-sc-epoint no diretório atual.
# O Dockerfile pode configurar o contêiner com um ponto de entrada (ENTRYPOINT) ou comando (CMD), 
# que será executado quando o contêiner for iniciado.
docker build -t ubuntu-curl -f Dockerfile15-sc-epoint .

# Executa um contêiner a partir da imagem "ubuntu-curl" usando o comando padrão configurado no Dockerfile.
# O contêiner será iniciado com o ponto de entrada ou comando configurado no Dockerfile.
docker container run ubuntu-curl 

# Executa outro contêiner a partir da imagem "ubuntu-curl" passando "teste" como argumento.
# Dependendo da configuração no Dockerfile, "teste" pode ser passado para o comando definido no ENTRYPOINT ou CMD.
docker container run ubuntu-curl teste

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço no sistema.
docker image prune
```
### SCRIPT ENTRYPOINT
### Dockerfile16-mix
[Dockerfile16-mix](curl/Dockerfile16-mix)

```docker
# Constrói a imagem Docker chamada "ubuntu-curl" a partir do Dockerfile16-mix no diretório atual.
# O Dockerfile pode combinar diferentes diretivas, como ENTRYPOINT, CMD, ou outras configurações,
# para configurar o comportamento do contêiner quando ele for executado.
docker build -t ubuntu-curl -f Dockerfile16-mix .

# Executa um contêiner a partir da imagem "ubuntu-curl" usando o comando padrão configurado no Dockerfile.
# O comando ou ponto de entrada especificado no Dockerfile será executado automaticamente ao iniciar o contêiner.
docker container run ubuntu-curl 

# Executa outro contêiner a partir da imagem "ubuntu-curl" passando "teste" como argumento.
# Se o Dockerfile configurar um ENTRYPOINT, o argumento "teste" será passado para ele.
docker container run ubuntu-curl teste

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo), liberando espaço no sistema.
docker image prune
```

### PRINCIPAIS COMANDOS COM IMAGENS
```docker
# Cria uma nova imagem a partir de um contêiner existente. 
# O comando "docker commit" cria uma imagem a partir do estado atual de um contêiner.
# O formato é: docker commit <container_id> <image_name>
docker commit <container_id> <image_name>

# Constrói uma imagem Docker a partir de um Dockerfile. 
# O comando "docker build" usa o Dockerfile no diretório atual (ou no caminho especificado) 
# para criar uma nova imagem Docker.
# O formato é: docker build -t <image_name> <path_to_dockerfile_directory>
docker build -t <image_name> <path_to_dockerfile_directory>

# Lista todas as imagens Docker disponíveis localmente.
# O comando "docker image ls" exibe uma lista de imagens armazenadas localmente, mostrando informações como 
# o nome da imagem, ID, data de criação e tamanho.
docker image ls

# Remove uma ou mais imagens Docker locais. 
# O comando "docker image rm" remove a imagem especificada, liberando espaço no sistema.
# O formato é: docker image rm <image_name_or_id>
docker image rm <image_name_or_id>

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
# O comando "docker container rm -f $(docker container ls -qa)" remove todos os contêineres listados 
# por "docker container ls -qa", ou seja, todos os contêineres (ativos ou não).
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais. 
# O comando "docker image rm -f $(docker image ls -qa)" força a remoção de todas as imagens 
# que estão listadas por "docker image ls -qa", ou seja, todas as imagens no sistema.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a contêineres) e que não estão em uso.
# O comando "docker image prune" libera espaço, removendo imagens que não estão mais associadas 
# a contêineres ativos ou inativos.
docker image prune
```
## Todos os arquivos Dockerfile desta parte estão dentro da pasta temperatura/src/
### IMAGEM DA APLICAÇÃO COM DOCKERFILE
### Dockerfile01
[Dockerfile01](temperatura/src/Dockerfile01)

```docker
# Navega até o diretório src onde está localizado o Dockerfile.
cd ~/devops/temperatura/src/

# Constrói uma imagem Docker chamada "conversao-temperatura" usando o Dockerfile01. 
# A opção "-f" especifica qual Dockerfile usar (neste caso, Dockerfile01).
docker build -t conversao-temperatura -f Dockerfile01 .

# Lista todas as imagens Docker locais disponíveis, mostrando informações como nome, ID, data de criação e tamanho.
docker image ls

# Executa um contêiner a partir da imagem "conversao-temperatura" em segundo plano (-d), 
# e mapeia a porta 8080 do contêiner para a porta 8080 do host.
docker container run -d -p 8080:8080 conversao-temperatura

# Lista todos os contêineres em execução. A opção "docker container ls" mostra contêineres ativos.
docker container ls

# Remove todos os contêineres Docker, forçando a remoção de contêineres em execução ou parados.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não associadas a nenhum contêiner ativo) e que não estão mais em uso.
docker image prune
```
## Docker Registry

### Alterando nome da imagem para ficar com nomenclatura correta
```docker
# Cria uma nova tag para a imagem "conversao-temperatura", associando a tag "fagnerfgb/conversao-temperatura:v1" à imagem.
# Isso é útil para versionamento e facilitar o gerenciamento de imagens.
docker tag conversao-temperatura fagnerfgb/conversao-temperatura:v1

# Lista todas as imagens Docker locais, mostrando informações como nome, ID, data de criação e tamanho.
docker image ls

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens (mesmo aquelas em uso).
# O comando "docker image rm -f $(docker image ls -qa)" seleciona todas as imagens e as remove.
docker image rm -f $(docker image ls -qa)

# Remove as imagens órfãs (não associadas a contêineres ativos). 
# Isso ajuda a liberar espaço, excluindo imagens que não são mais necessárias.
docker image prune
```

### Criando imagem com a nomenclatura correta para envio ao DockerHub
```docker
# Navega até o diretório src onde o Dockerfile e o código do projeto de conversão de temperatura estão localizados.
cd ~/devops/temperatura/src/

# Constrói a imagem Docker chamada "fagnerfgb/conversao-temperatura:v1" usando o Dockerfile01.
# A tag "v1" é usada para identificar esta versão específica da imagem.
docker build -t fagnerfgb/conversao-temperatura:v1 -f Dockerfile01 .

# Cria uma nova tag para a imagem "fagnerfgb/conversao-temperatura:v1", 
# associando a tag "fagnerfgb/conversao-temperatura:latest" à mesma imagem.
# A tag "latest" geralmente representa a versão mais recente ou estável da imagem.
docker tag fagnerfgb/conversao-temperatura:v1 fagnerfgb/conversao-temperatura:latest
```
### Enviar imagem ao DockerHub
```docker
# Solicita o login do Docker para autenticar o usuário no Docker Hub ou outro repositório Docker.
# Você será solicitado a inserir seu nome de usuário e senha.
docker login

# Envia a imagem "fagnerfgb/conversao-temperatura:v1" para o repositório Docker Hub (ou outro repositório remoto configurado).
# Isso torna a imagem disponível para download por outros usuários ou sistemas.
docker push fagnerfgb/conversao-temperatura:v1

# Envia a imagem "fagnerfgb/conversao-temperatura:latest" para o repositório Docker Hub (ou outro repositório remoto configurado).
# A tag "latest" é usada para marcar a versão mais recente da imagem.
docker push fagnerfgb/conversao-temperatura:latest

# Remove todas as imagens Docker locais. Isso pode ser útil para liberar espaço ou limpar imagens antigas.
# A opção "-f" força a remoção das imagens, e "docker image ls -qa" seleciona todas as imagens presentes no sistema.
docker image rm -f $(docker image ls -qa)

# Remove imagens que não estão sendo usadas por nenhum contêiner ativo.
# Isso pode liberar espaço no sistema excluindo imagens órfãs que não estão mais em uso.
docker image prune

# Baixa a imagem "fagnerfgb/conversao-temperatura" do repositório remoto para o sistema local.
# Isso pode ser útil para garantir que você tenha a versão mais recente da imagem.
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
# Constrói a imagem "fagnerfgb/conversao-temperatura:v2" usando o Dockerfile-alpine01.
# O uso de "alpine" no nome do Dockerfile sugere que a imagem será baseada na imagem oficial Alpine Linux, que é leve e otimizada.
docker build -t fagnerfgb/conversao-temperatura:v2 -f Dockerfile-alpine01 .

# Cria uma nova tag "latest" para a imagem "fagnerfgb/conversao-temperatura:v2".
# A tag "latest" é frequentemente usada para referir a versão mais recente da imagem.
docker tag fagnerfgb/conversao-temperatura:v2 fagnerfgb/conversao-temperatura:latest

# Executa o contêiner em segundo plano, expondo a porta 8080 do contêiner para a porta 8080 da máquina host.
# Isso permite que a aplicação seja acessada via navegador ou outras ferramentas na porta 8080.
docker container run -d -p 8080:8080 fagnerfgb/conversao-temperatura:v2

# Remove todos os contêineres Docker em execução ou parados.
# A opção "-f" força a remoção de contêineres sem a necessidade de confirmação.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais.
# A opção "-f" força a remoção de todas as imagens, e "docker image ls -qa" seleciona todas as imagens presentes no sistema.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs, ou seja, imagens que não estão associadas a contêineres ativos.
# Esse comando pode ser usado para limpar imagens não utilizadas e liberar espaço.
docker image prune
```
## Multistage build
### Criando imagem simples do GoLang com a nossa aplicação
## Todos os arquivos Dockerfile desta parte estão dentro da pasta golang

### Dockerfile.simples
[Dockerfile.simples](golang/Dockerfile.simples)

```docker
# Atualiza o repositório local com as últimas mudanças do repositório remoto.
# Isso garante que você tenha a versão mais recente dos arquivos do projeto.
cd ~/devops
git pull

# Muda para o diretório do projeto Golang.
# Esse diretório provavelmente contém o código e o Dockerfile para construir a aplicação.
cd ~/devops/golang

# Constrói a imagem Docker chamada "fagnerfgb/app-multi-staging:simples" usando o Dockerfile "Dockerfile.simples".
# O parâmetro "-f Dockerfile.simples" especifica qual Dockerfile será usado para a construção.
docker build -t fagnerfgb/app-multi-staging:simples -f Dockerfile.simples .

# Executa o contêiner em segundo plano, expondo a porta 8080 do contêiner para a porta 8080 da máquina host.
# Isso permite que a aplicação no contêiner seja acessada via navegador ou outras ferramentas.
docker run -d -p 8080:8080 fagnerfgb/app-multi-staging:simples 

# Remove todos os contêineres Docker locais, tanto em execução quanto parados.
# A opção "-f" força a remoção sem a necessidade de confirmação.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais.
# A opção "-f" força a remoção de todas as imagens, e "docker image ls -qa" seleciona todas as imagens presentes no sistema.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não usadas por nenhum contêiner ativo).
# Este comando pode ser usado para liberar espaço, removendo imagens que não estão sendo utilizadas.
docker image prune
```
### Dockerfile.multistage
[Dockerfile.multistage](golang/Dockerfile.multistage)

```docker
# Constrói a imagem Docker chamada "fagnerfgb/app-multistaging:multi" 
# usando o Dockerfile "Dockerfile.multistage". A construção de uma imagem multi-stage 
# geralmente é usada para otimizar o processo, minimizando o tamanho da imagem final.
docker build -t fagnerfgb/app-multistaging:multi -f Dockerfile.multistage .

# Executa o contêiner da imagem "fagnerfgb/app-multistaging:multi" em segundo plano, 
# mapeando a porta 8080 do contêiner para a porta 8080 da máquina host.
docker container run -d -p 8080:8080 fagnerfgb/app-multistaging:multi

# Remove todos os contêineres locais, tanto em execução quanto parados.
# A opção "-f" força a remoção sem a necessidade de confirmação.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais. A opção "-f" força a remoção de todas as imagens.
# O comando "docker image ls -qa" seleciona todas as imagens no sistema.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não usadas por contêineres ativos). 
# Este comando pode ser útil para liberar espaço removendo imagens antigas ou não usadas.
docker image prune
```

### Construindo a imagem intermediária "build"
### Dockerfile.multistage
[Dockerfile.multistage](golang/Dockerfile.multistage)

```docker
# Constrói a imagem Docker chamada "fagnerfgb/app-multistaging:multi" 
# a partir do Dockerfile "Dockerfile.multistage", usando a etapa de construção 
# especificada pela opção "--target=build". Isso permite que você construa a imagem 
# até um ponto específico (neste caso, até a etapa de "build"), sem precisar passar 
# por todas as etapas subsequentes no Dockerfile.
docker build -t fagnerfgb/app-multistaging:multi -f Dockerfile.multistage --target=build .

# Executa o contêiner da imagem "fagnerfgb/app-multistaging:multi" em segundo plano, 
# mapeando a porta 8080 do contêiner para a porta 8080 da máquina host.
docker container run -d -p 8080:8080 fagnerfgb/app-multistaging:multi

# Remove todos os contêineres locais, tanto em execução quanto parados.
# A opção "-f" força a remoção sem a necessidade de confirmação.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais. A opção "-f" força a remoção de todas as imagens.
# O comando "docker image ls -qa" seleciona todas as imagens no sistema.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs (não usadas por contêineres ativos). 
# Este comando pode ser útil para liberar espaço removendo imagens antigas ou não usadas.
docker image prune
```

### Copiar arquivos de outras imagens
### Dockerfile.pacote-bin
[Dockerfile.pacote-bin](golang/Dockerfile.pacote-bin)

```docker
# Executa um contêiner a partir da imagem "fabricioveronez/pacote-bin:v1" 
# em modo interativo (-it), com um shell (/bin/sh) para interação com o contêiner.
docker container run -it fabricioveronez/pacote-bin:v1 /bin/sh

# Lista os arquivos e diretórios no diretório atual dentro do contêiner.
ls

# Sai do contêiner e retorna ao ambiente local.
exit
```
```docker
docker build -t fagnerfgb/# Constrói a imagem Docker "fagnerfgb/app-multistaging-copia:multistaging" 
# a partir do Dockerfile "Dockerfile.pacote-bin". Essa imagem é uma cópia da imagem multistaging original.
docker build -t fagnerfgb/app-multistaging-copia:multistaging -f Dockerfile.pacote-bin .

# Executa o contêiner da imagem recém-criada em modo "detached" (-d) e mapeia a porta 8080 do contêiner 
# para a porta 8080 do host. O contêiner será executado em segundo plano.
docker container run -d -p 8080:8080 fagnerfgb/app-multistaging-copia:multistaging

# Lista os contêineres em execução. O comando exibe o ID do contêiner, a imagem usada e outras informações.
docker container ls

# Executa um shell interativo (/bin/sh) dentro do contêiner com ID "4156db95e96f".
# Isso permite que você execute comandos diretamente dentro do contêiner.
docker container exec -it 4156db95e96f /bin/sh

# Lista os arquivos e diretórios no diretório atual dentro do contêiner.
ls

# Sai do shell interativo dentro do contêiner.
exit

# Remove todos os contêineres locais, sejam eles ativos ou parados.
# A opção "-f" força a remoção sem a necessidade de confirmação.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, com a opção "-f" para forçar a remoção das imagens.
# O comando "docker image ls -qa" seleciona todas as imagens no sistema.
docker image rm -f $(docker image ls -qa)

# Remove as imagens órfãs (não usadas por contêineres ativos) para liberar espaço no sistema.
docker image prune
```

### Usando imagem intermediária como base para outra imagem
### Dockerfile.intermediaria
[Dockerfile.intermediaria](golang/Dockerfile.intermediaria)

```docker
# Constrói a imagem Docker chamada "fagnerfgb/app-multistaging-intermediaria:intermediaria"
# a partir do Dockerfile "Dockerfile.intermediaria". Esta imagem intermediária é parte do processo multistage.
docker build -t fagnerfgb/app-multistaging-intermediaria:intermediaria -f Dockerfile.intermediaria .

# Executa o contêiner da imagem recém-criada em modo "detached" (-d), mapeando a porta 8080 do contêiner 
# para a porta 8080 do host. O contêiner será executado em segundo plano.
docker container run -d -p 8080:8080 fagnerfgb/app-multistaging-intermediaria:intermediaria

# Lista os contêineres em execução, exibindo o ID do contêiner, a imagem utilizada e outras informações.
docker container ls

# Executa um shell interativo (/bin/sh) dentro do contêiner com ID "c8ab0638f446".
# Isso permite que você execute comandos diretamente dentro do contêiner.
docker container exec -it c8ab0638f446 /bin/sh

# Lista os arquivos e diretórios no diretório atual dentro do contêiner.
ls

# Sai do shell interativo dentro do contêiner.
exit

# Remove todos os contêineres locais, sejam eles ativos ou parados. 
# A opção "-f" força a remoção sem a necessidade de confirmação.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, com a opção "-f" para forçar a remoção das imagens.
# O comando "docker image ls -qa" seleciona todas as imagens no sistema.
docker image rm -f $(docker image ls -qa)

# Remove as imagens órfãs (não usadas por contêineres ativos) para liberar espaço no sistema.
docker image prune
```

## Volumes
### Bind Mount
Mapeia um diretório sistema de arquivo do host com um diretório do container

```docker
# Cria um diretório chamado "aula_volume" no diretório atual
mkdir aula_volume

# Executa um contêiner Ubuntu, montando o diretório "aula_volume" do host 
# no diretório "/app" dentro do contêiner. O contêiner é executado com um shell interativo (/bin/bash).
docker container run -it --mount type=bind,source="$(pwd)/aula_volume",target=/app ubuntu /bin/bash

# Dentro do contêiner, cria um arquivo de texto chamado "teste.txt" no diretório /app.
# O conteúdo "Teste" é escrito nesse arquivo.
echo "Teste" > /app/teste.txt

# Remove todos os contêineres, incluindo os parados. A opção "-f" força a remoção.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais. A opção "-f" força a remoção.
docker image rm -f $(docker image ls -qa)

# Remove as imagens órfãs (não usadas por contêineres ativos) para liberar espaço no sistema.
docker image prune
```

[Dockerfile-bind](aula_volume/Dockerfile-bind)
```docker
# Constrói uma imagem Docker chamada "fagnerfgb/volume-bind:v1"
# Usando o Dockerfile localizado no diretório "aula_volume/Dockerfile-bind"
docker build -t fagnerfgb/volume-bind:v1 -f aula_volume/Dockerfile-bind .

# Executa um contêiner a partir da imagem "fagnerfgb/volume-bind:v1"
# Montando o diretório "aula_volume" no diretório "/app" dentro do contêiner.
# O contêiner é executado com um shell interativo (/bin/bash).
docker container run -it --mount type=bind,source="$(pwd)/aula_volume",target=/app fagnerfgb/volume-bind:v1 /bin/bash

# Remove todos os contêineres, incluindo os que estão parados.
# A opção "-f" força a remoção sem confirmação.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais. A opção "-f" força a remoção.
docker image rm -f $(docker image ls -qa)

# Remove as imagens órfãs (não usadas por contêineres ativos), liberando espaço no sistema.
docker image prune
```

### Bind de diretório
```docker
# Executa um contêiner em segundo plano (-d), mapeando a porta 8080 do host para a porta 80 do contêiner.
# Monta o diretório local "$(pwd)/aula_volume/html" para o diretório "/usr/share/nginx/html" dentro do contêiner,
# que é o local onde o Nginx espera os arquivos HTML.
# O contêiner executa a imagem "nginx", servindo conteúdo web no diretório especificado.
docker container run -d -p 8080:80 -v $(pwd)/aula_volume/html:/usr/share/nginx/html nginx

# Remove todos os contêineres, incluindo os que estão parados.
# A opção "-f" força a remoção sem confirmação.
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais. A opção "-f" força a remoção.
docker image rm -f $(docker image ls -qa)

# Remove as imagens órfãs (não usadas por contêineres ativos), liberando espaço no sistema.
docker image prune
```

### Bind de arquivo
```docker
# Executa um contêiner Nginx em segundo plano, mapeando a porta 8080 do host para a porta 80 do contêiner
# E substituindo o arquivo index.html padrão do Nginx pelo arquivo localizado em aula_volume/html/index.html
docker container run -d -p 8080:80 -v $(pwd)/aula_volume/html/index.html:/usr/share/nginx/html/index.html nginx

# Remove todos os contêineres, incluindo os contêineres em execução e os parados
# A opção -f força a remoção sem a necessidade de confirmação
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais
# A opção -f força a remoção das imagens, mesmo que estejam em uso por contêineres
docker image rm -f $(docker image ls -qa)

# Limpa as imagens órfãs (não utilizadas por nenhum contêiner ativo)
# Isso ajuda a liberar espaço no sistema
docker image prune
```

### Docker Volume
Gerenciado pelo docker

#### Comandos básicos
```docker
# Cria um volume Docker chamado 'aula_volume', utilizado para persistir dados entre contêineres
docker volume create aula_volume

# Lista todos os volumes Docker disponíveis no sistema
docker volume ls

# Inspeciona o volume 'aula_volume' para exibir informações detalhadas, como caminho de armazenamento, contêineres associados, etc.
docker volume inspect aula_volume

# Remove o volume 'aula_volume', liberando o espaço que estava sendo utilizado por ele
docker volume rm aula_volume
```
```docker
# Cria um volume Docker chamado 'aula_volume', utilizado para persistir dados entre contêineres
docker volume create aula_volume

# Executa um contêiner Ubuntu, montando o volume 'aula_volume' no diretório '/app' dentro do contêiner
# O tipo 'volume' faz o contêiner usar o volume Docker, garantindo persistência de dados
docker container run -it --mount type=volume,source=aula_volume,target=/app ubuntu /bin/bash

# Remove todos os contêineres, incluindo os contêineres em execução e os parados
# A opção -f força a remoção sem a necessidade de confirmação
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais
# A opção -f força a remoção das imagens, mesmo que estejam em uso por contêineres
docker image rm -f $(docker image ls -qa)

# Limpa as imagens órfãs (não utilizadas por nenhum contêiner ativo)
# Isso ajuda a liberar espaço no sistema
docker image prune
```
```docker
# Lista todos os volumes Docker disponíveis no sistema
docker volume ls

# Exibe informações detalhadas sobre o volume 'aula_volume', como o caminho do armazenamento e as configurações
docker volume inspect aula_volume

# Remove volumes que não estão mais em uso por nenhum contêiner
# Isso ajuda a liberar espaço no sistema removendo volumes órfãos
docker volume prune
```

[Dockerfile-volume](aula_volume/Dockerfile-volume)


```docker
# Constrói a imagem 'fagnerfgb/volume:v1' a partir do Dockerfile localizado em 'aula_volume/Dockerfile-volume'
docker build -t fagnerfgb/volume:v1 -f aula_volume/Dockerfile-volume .

# O comando abaixo roda um contêiner da imagem 'fagnerfgb/volume:v1' interativamente, 
# mas como o Dockerfile especifica a criação de um volume, 
# o Docker cria um volume com um ID aleatório, pois não é especificado um volume específico
docker container run -it fagnerfgb/volume:v1 /bin/bash
exit

# Lista todos os volumes criados no sistema Docker, 
# incluindo o volume gerado automaticamente pelo comando anterior
docker volume ls

# Aqui, o contêiner é executado com um volume específico montado na pasta '/app'
# Neste caso, 'aula_volume' é o volume que foi criado anteriormente,
# e será montado no contêiner na pasta '/app'
docker container run -it -v aula_volume:/app fagnerfgb/volume:v1 /bin/bash

# Remove todos os contêineres, forçando a remoção mesmo que estejam em execução
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker não utilizadas
docker image rm -f $(docker image ls -qa)

# Limpa as imagens órfãs que não estão mais associadas a nenhum contêiner
docker image prune

# Remove volumes órfãos que não estão sendo usados por nenhum contêiner
docker volume prune
```

### Backup de um docker volume
```docker
# O comando 'docker build' cria uma imagem chamada 'fagnerfgb/volume:v1' a partir do Dockerfile 
# localizado em 'aula_volume/Dockerfile-volume'. Esse Dockerfile inclui a instrução para criar um volume.
# Como o comando abaixo não faz referência a um volume específico, o Docker cria automaticamente um volume
# com um ID aleatório e o monta dentro do contêiner quando ele é executado.
docker build -t fagnerfgb/volume:v1 -f aula_volume/Dockerfile-volume .

# O comando 'docker container run' executa o contêiner da imagem 'fagnerfgb/volume:v1' de forma interativa 
# e executa o shell '/bin/bash' dentro do contêiner. Neste caso, um volume aleatório criado durante a construção 
# da imagem será automaticamente montado dentro do contêiner.
docker container run -it fagnerfgb/volume:v1 /bin/bash
```

```docker
# O comando cria um arquivo chamado 'teste.txt' com o conteúdo 'Teste'.
echo "Teste" > teste.txt

# O comando cria um arquivo chamado 'exemplo.txt' com o conteúdo 'Exemplo'.
echo "Exemplo" > exemplo.txt

# O comando 'exit' sai do contêiner, encerrando a sessão interativa.
exit
```

```docker
# Exibe todos os contêineres, incluindo os parados
docker container ls -a

# --volumes-from id --> pega todos os volumes do contêiner do passo anterior 
# e coloca dentro do novo contêiner criado
docker container run --volumes-from 823a0c12800b --rm -v $(pwd):/backup fagnerfgb/volume:v1 tar cvf /backup/bkp_vol.tar /app

# Cria um volume com o nome "novo_volume"
docker volume create novo_volume

# Restaura o backup no novo contêiner, colocando os dados no volume "novo_volume"
docker container run -v $(pwd):/backup -v novo_volume:/app fagnerfgb/volume:v1 tar xvf /backup/bkp_vol.tar

# Remove todos os contêineres, tanto em execução quanto parados
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens não utilizadas
docker image rm -f $(docker image ls -qa)

# Limpa todas as imagens não utilizadas
docker image prune

# Limpa todos os volumes não utilizados
docker volume prune
```

### Exemplo com um docker volume (Bind)
```docker
# Cria um diretório chamado db_vol para ser usado como volume
mkdir db_vol

# Cria e executa um contêiner com o PostgreSQL
# - O contêiner é executado em segundo plano (-d)
# - Mapeia a porta 5432 do contêiner para a porta 5432 da máquina host (-p 5432:5432)
# - Define a variável de ambiente POSTGRES_PASSWORD com o valor "docker_pwd"
# - Usa o tipo de volume "bind" para vincular o diretório local db_vol ao diretório do contêiner /var/lib/postgresql/data, onde o PostgreSQL armazena seus dados
docker container run -d -p 5432:5432 -e POSTGRES_PASSWORD="docker_pwd" --mount type=bind,source="$(pwd)/db_vol",target=/var/lib/postgresql/data postgres

# Remove todos os contêineres, tanto em execução quanto parados
docker container rm -f $(docker container ls -qa)
```

### Exemplo com um docker volume (Volume)
```docker
# Cria e executa um contêiner PostgreSQL com volume nomeado
# - O contêiner é executado em segundo plano (-d)
# - Mapeia a porta 5432 do contêiner para a porta 5432 da máquina host (-p 5432:5432)
# - Define a variável de ambiente POSTGRES_PASSWORD com o valor "docker_pwd"
# - Usa um volume nomeado "container_postgre_vol" para armazenar os dados do PostgreSQL em vez de usar bind mount
docker container run -d -p 5432:5432 -e POSTGRES_PASSWORD="docker_pwd" --mount type=volume,source=container_postgre_vol,target=/var/lib/postgresql/data postgres

# Remove todos os contêineres, tanto em execução quanto parados
docker container rm -f $(docker container ls -qa)
```
```docker
# Remove todas as imagens do Docker, forçando a remoção de todas as imagens, incluindo aquelas sem tags.
docker image rm -f $(docker image ls -qa)

# Remove todas as imagens não utilizadas, ou seja, imagens que não estão associadas a containers em execução.
docker image prune

# Remove todos os volumes do Docker que não estão sendo utilizados por nenhum container.
docker volume prune
```

### Exemplo com tmpfs
```docker
# Cria e executa um container baseado na imagem ubuntu:22.04, montando um sistema de arquivos temporário (tmpfs) em /app dentro do container.
# Isso faz com que o diretório /app seja armazenado na memória volátil do host, não persistindo após o container ser removido.
docker container run -it --mount type=tmpfs,target=/app ubuntu:22.04 /bin/bash
```

### Postgres
```docker
# Cria e executa um container PostgreSQL, mapeando a porta 5432, definindo variáveis de ambiente para senha, usuário e banco de dados.
# O volume 'kubenews_vol' é montado para persistência dos dados em /var/lib/postgresql/data.
docker container run -d -p 5432:5432 -e POSTGRES_PASSWORD="pwdkubenews" -e POSTGRES_USER=kubenews -e POSTGRES_DB=kubenews -v kubenews_vol:/var/lib/postgresql/data postgres:14.10

# Remove todos os containers que estão parados ou em execução, forçando a remoção sem confirmação
docker container rm -f $(docker container ls -qa)
```


### Executando aplicação nodejs em servidor comum
```docker
# Atualiza a lista de pacotes disponíveis para instalação
sudo apt update

# Instala o Node.js e o npm (gerenciador de pacotes do Node.js)
sudo apt install nodejs -y && sudo apt install npm -y

# Verifica a versão do Node.js instalada
node -v

# Navega até o diretório do projeto 'kube-news'
cd ~/devops/kube-news/src/

# Instala todas as dependências listadas no arquivo 'package.json'
npm install

# Corrige automaticamente vulnerabilidades e problemas encontrados nas dependências
npm audit fix

# Inicia o servidor Node.js com o script 'server.js'
node server.js
```
```docker
# Remove todos os contêineres, independentemente de estarem em execução ou não
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens, mesmo que estejam em uso por contêineres
docker image rm -f $(docker image ls -qa)

# Limpa imagens que não estão mais sendo usadas por contêineres, liberando espaço
docker image prune

# Limpa volumes não utilizados, ou seja, volumes não associados a nenhum contêiner
docker volume prune
```
### Network
```docker
# Lista todas as redes Docker disponíveis no sistema
docker network ls

# Exibe detalhes sobre a rede Docker com o ID "67ec744aeba4"
docker network inspect 67ec744aeba4

# Executa o contêiner "nginx" em segundo plano (-d), iniciando um servidor web Nginx
docker container run -d nginx

# Lista todos os contêineres em execução no momento, mostrando informações como ID, nome e estado
docker container ls

# Exibe detalhes completos sobre o contêiner com o ID "acb4df8a0f90"
docker container inspect acb4df8a0f90

# Executa o contêiner "ubuntu" em modo interativo (-it) e abre o terminal bash dentro do contêiner
docker container run -it ubuntu /bin/bash
```
```docker
# Atualiza a lista de pacotes disponíveis e instala o curl no sistema
apt update && apt install curl -y

# Faz uma requisição HTTP para o endereço IP 172.17.0.2 (pode ser um contêiner Docker ou outro serviço na rede)
curl http://172.17.0.2

# Sai do terminal ou contêiner atual
exit
```
```docker
# Remove todos os contêineres Docker, forçando a remoção de contêineres em execução ou parados
# O comando $(docker container ls -qa) lista os IDs de todos os contêineres (ativos ou não)
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens
# O comando $(docker image ls -qa) lista os IDs de todas as imagens
docker image rm -f $(docker image ls -qa)

# Remove imagens não utilizadas ou órfãs, que não estão mais associadas a contêineres
docker image prune
```
### Criando Rede Bridge
```docker
# Cria uma rede Docker chamada "aula_docker"
docker network create aula_docker

# Lista todas as redes Docker disponíveis no sistema
docker network ls

# Exibe detalhes sobre a rede Docker chamada "aula_docker"
docker network inspect aula_docker

# Executa um contêiner Nginx em segundo plano (-d) com o nome "fgb-nginx"
docker container run --name fgb-nginx -d nginx

# Executa um contêiner Ubuntu em modo interativo (-it) com o nome "fgb-ubuntu", 
# e abre o terminal bash dentro do contêiner
docker container run --name fgb-ubuntu -it ubuntu /bin/bash
```
```docker
# Atualiza a lista de pacotes disponíveis e instala o curl no sistema
apt update && apt install curl -y

# Comentário explicativo: Não há comunicação porque a rede "aula_docker" não foi configurada
# para ser utilizada pelos contêineres, por isso o contêiner "fgb-nginx" não é acessível diretamente.
# Para que a comunicação seja possível, o contêiner precisa ser conectado à rede "aula_docker" explicitamente.

# Faz uma requisição HTTP para o contêiner "fgb-nginx" através de sua rede. 
# Isso não funcionará se o contêiner não estiver conectado à rede "aula_docker".
curl http://fgb-nginx

# Sai do terminal ou contêiner atual
exit
```
```docker
# Conecta o contêiner "fgb-nginx" à rede "aula_docker"
docker network connect aula_docker fgb-nginx

# Exibe detalhes sobre o contêiner "fgb-nginx", incluindo redes conectadas
docker container inspect fgb-nginx

# Desconecta o contêiner "fgb-nginx" da rede padrão "bridge"
docker network disconnect bridge fgb-nginx

# Exibe novamente detalhes sobre o contêiner "fgb-nginx" para verificar as redes conectadas
docker container inspect fgb-nginx

# Conecta o contêiner "fgb-ubuntu" à rede "aula_docker"
docker network connect aula_docker fgb-ubuntu

# Desconecta o contêiner "fgb-ubuntu" da rede padrão "bridge"
docker network disconnect bridge fgb-ubuntu

# Exibe detalhes sobre o contêiner "fgb-ubuntu" para verificar as redes conectadas
docker container inspect fgb-ubuntu
```
```docker
# Agora há comunicação entre os contêineres, pois ambos estão conectados à rede "aula_docker"
# Isso permite que o contêiner "fgb-ubuntu" acesse o contêiner "fgb-nginx" via IP ou nome do contêiner.

# Faz uma requisição HTTP para o contêiner "fgb-nginx" via rede "aula_docker"
curl http://fgb-nginx

# Sai do terminal ou contêiner atual
exit
```

```docker
# Cria uma nova rede Docker chamada "outra_rede_docker" com o intervalo de IP 10.0.0.0/16 e o gateway 10.0.0.1
docker network create --subnet=10.0.0.0/16 --gateway=10.0.0.1 outra_rede_docker

# Lista todas as redes Docker disponíveis, incluindo a nova rede "outra_rede_docker"
docker network ls

# Exibe detalhes sobre a rede "outra_rede_docker", incluindo configuração e contêineres conectados
docker network inspect outra_rede_docker

# Executa um contêiner Nginx em segundo plano (-d), nomeando-o como "fgb-nginx-2" e conectando-o à rede "outra_rede_docker"
docker container run -d --name fgb-nginx-2 --network outra_rede_docker nginx

# Executa um contêiner Ubuntu em modo interativo (-it), nomeando-o como "fgb-ubuntu-2" e conectando-o à rede "outra_rede_docker",
# abrindo o terminal bash dentro do contêiner
docker container run --name fgb-ubuntu-2 --network outra_rede_docker -it ubuntu /bin/bash
```

```docker
# Atualiza a lista de pacotes disponíveis e instala o curl no sistema
apt update && apt install curl -y

# Agora há comunicação entre os contêineres porque ambos estão conectados à rede "outra_rede_docker"
# Isso permite que o contêiner "fgb-ubuntu-2" acesse o contêiner "fgb-nginx-2" via IP ou nome do contêiner.

# Faz uma requisição HTTP para o contêiner "fgb-nginx-2" via rede "outra_rede_docker"
curl http://fgb-nginx-2

# Sai do terminal ou contêiner atual
exit
```
```docker
# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
# O comando $(docker container ls -qa) lista todos os IDs dos contêineres (ativos ou não).
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
# O comando $(docker image ls -qa) lista todos os IDs das imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs, ou seja, imagens não utilizadas por nenhum contêiner.
# Essa ação limpa imagens que não são mais necessárias e não estão associadas a contêineres ativos.
docker image prune
```

```docker
# Remove a rede personalizada 'aula_docker'
docker network rm aula_docker

# Remove todas as redes não utilizadas
docker network prune

# Lista todas as redes disponíveis no Docker
docker network ls

# Exibe as informações de endereço IP do sistema
ip address

# Inspeciona a rede 'bridge' (rede padrão do Docker)
docker network inspect bridge

# Cria uma nova rede personalizada chamada 'aula_docker'
docker network create aula_docker

# Exibe as informações de endereço IP novamente para verificar alterações
ip a

# Inspeciona a rede recém-criada 'aula_docker'
docker network inspect aula_docker

# Executa um contêiner Nginx em segundo plano
docker container run -d nginx

# Exibe as informações de endereço IP novamente
ip a

# Mostra o status das pontes de rede
bridge link

# Executa outro contêiner Nginx em segundo plano
docker container run -d nginx

# Lista todos os contêineres em execução
docker container ls

# Exibe as informações de endereço IP novamente
ip a

# Conecta o contêiner especificado à rede 'aula_docker'
docker network connect aula_docker 754214f895fd

# Exibe as informações de endereço IP novamente
ip a

# Mostra o status das pontes de rede novamente
bridge link

# Desconecta o contêiner da rede 'bridge'
docker network disconnect bridge 754214f895fd

# Mostra o status das pontes de rede após a desconexão
bridge link

# Exibe as informações de endereço IP novamente
ip a

# Remove todas as redes não utilizadas
docker network prune

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
# O comando $(docker container ls -qa) lista todos os IDs dos contêineres (ativos ou não).
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
# O comando $(docker image ls -qa) lista todos os IDs das imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs, ou seja, imagens não utilizadas por nenhum contêiner.
# Essa ação limpa imagens que não são mais necessárias e não estão associadas a contêineres ativos.
docker image prune
```
### Rede Host
```docker
# Executa um contêiner Nginx em segundo plano usando a rede 'host'
docker container run -d --network=host nginx

# Lista todos os contêineres em execução
docker container ls

# Inspeciona o contêiner com o ID especificado (neste exemplo: 04bcc220199b)
docker container inspect 04bcc220199b

# Exibe as informações de endereço IP do sistema para verificar como a rede 'host' está configurada
ip a

# Remove todas as redes não utilizadas
docker network prune

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
# O comando $(docker container ls -qa) lista todos os IDs dos contêineres (ativos ou não).
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
# O comando $(docker image ls -qa) lista todos os IDs das imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs, ou seja, imagens não utilizadas por nenhum contêiner.
# Essa ação limpa imagens que não são mais necessárias e não estão associadas a contêineres ativos.
docker image prune
```
### Rede None
```docker
# Executa um contêiner Ubuntu em modo interativo e com rede desativada
docker container run -it --network=none ubuntu /bin/bash

```
```docker
# Lista todos os contêineres em execução
docker container ls

# Inspeciona o contêiner específico pelo ID ou nome
docker container inspect c818caeacf29
```
```docker
exit
```
```docker
# Remove todas as redes não utilizadas
docker network prune

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
# O comando $(docker container ls -qa) lista todos os IDs dos contêineres (ativos ou não).
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
# O comando $(docker image ls -qa) lista todos os IDs das imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs, ou seja, imagens não utilizadas por nenhum contêiner.
# Essa ação limpa imagens que não são mais necessárias e não estão associadas a contêineres ativos.
docker image prune
```
### Adicionar domínios ao container
```docker
# Exibe as informações das interfaces de rede do sistema host
ip a

# Cria e executa um contêiner chamado "fgb-nginx" com a imagem Nginx, utilizando a rede "host"
docker container run --name fgb-nginx -d --network=host nginx

# Cria e executa um contêiner chamado "fgb-ubuntu" com a imagem Ubuntu, adicionando uma entrada no arquivo /etc/hosts
# que associa o nome "fagner.com.br" ao endereço IP 172.31.111.24. Abre um shell interativo no contêiner.
docker container run --name fgb-ubuntu --add-host=fagner.com.br:172.31.111.24 -it ubuntu /bin/bash
```
```docker
# Atualiza a lista de pacotes disponíveis no contêiner
apt update 

# Instala o utilitário 'curl' no contêiner
apt install curl -y

# Usa o 'curl' para fazer uma requisição HTTP ao hostname 'fagner.com.br'
curl fagner.com.br

# Sai do contêiner e encerra o shell interativo
exit
```
```docker
# Remove todas as redes não utilizadas
docker network prune

# Remove todos os contêineres Docker, incluindo os contêineres em execução ou parados.
# O comando $(docker container ls -qa) lista todos os IDs dos contêineres (ativos ou não).
docker container rm -f $(docker container ls -qa)

# Remove todas as imagens Docker locais, forçando a remoção de todas as imagens.
# O comando $(docker image ls -qa) lista todos os IDs das imagens.
docker image rm -f $(docker image ls -qa)

# Remove imagens órfãs, ou seja, imagens não utilizadas por nenhum contêiner.
# Essa ação limpa imagens que não são mais necessárias e não estão associadas a contêineres ativos.
docker image prune
```