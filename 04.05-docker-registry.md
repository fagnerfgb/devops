#Autor: Fagner Geraldes Braga  
#Data de criação: 03/01/2025  
#Data de atualização: 03/01/2025  
#Versão: 0.01

## Docker Registry

### Alterando nome da imagem para ficar com nomenclatura correta
```bash
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
```bash
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
```bash
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

```bash
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