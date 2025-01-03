#Autor: Fagner Geraldes Braga  
#Data de criação: 03/01/2025  
#Data de atualização: 03/01/2025  
#Versão: 0.01

### Criando imagem com a aplicação
```docker
# Navega até o diretório do projeto contendo o código e o Dockerfile
cd ~/devops/kube-news/src/

# Constrói uma imagem Docker usando o Dockerfile no diretório atual, com a tag v1
docker build -t fagnerfgb/kube-news:v1 -f Dockerfile .

# Adiciona outra tag "latest" à mesma imagem, permitindo identificar a última versão
docker tag fagnerfgb/kube-news:v1 fagnerfgb/kube-news:latest

# Faz login no Docker Hub (necessário para enviar imagens)
docker login

# Envia a imagem com a tag v1 para o Docker Hub
docker push fagnerfgb/kube-news:v1

# Envia a imagem com a tag "latest" para o Docker Hub
docker push fagnerfgb/kube-news:latest

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
### Criando a rede kube_news_net
```docker
# Cria uma nova rede Docker chamada "kube_news_net"
docker network create kube_news_net

# Lista todas as redes disponíveis no Docker
docker network ls

# Inspeciona os detalhes da rede "kube_news_net"
docker network inspect kube_news_net

# Exibe as configurações de rede do sistema host
ip a
```
### Criando container Postgres
```docker
# Executa um contêiner PostgreSQL conectado à rede "kube_news_net"
docker container run \
  -d \                                  # Executa o contêiner em modo desacoplado (background)
  -p 5432:5432 \                        # Mapeia a porta 5432 do contêiner para a porta 5432 do host
  --name kube_news_db \                 # Nomeia o contêiner como "kube_news_db"
  -e POSTGRES_PASSWORD="pwdkubenews" \  # Define a senha do usuário padrão do PostgreSQL
  -e POSTGRES_USER=kubenews \           # Cria um usuário personalizado chamado "kubenews"
  -e POSTGRES_DB=kubenews \             # Cria um banco de dados inicial chamado "kubenews"
  --network=kube_news_net \             # Conecta o contêiner à rede Docker "kube_news_net"
  -v kube_news_vol:/var/lib/postgresql/data \  # Monta o volume "kube_news_vol" no diretório de dados do PostgreSQL
  postgres                              # Imagem do PostgreSQL a ser usada

# Lista todos os contêineres em execução
docker container ls

```
### Criando container da aplicação
```docker
docker container run -d \
  -p 8080:8080 \                         # Mapeia a porta 8080 do contêiner para a porta 8080 do host
  -e DB_DATABASE=kubenews \               # Define o nome do banco de dados a ser usado no aplicativo
  -e DB_USERNAME=kubenews \               # Define o nome de usuário para acessar o banco de dados
  -e DB_PASSWORD=pwdkubenews \            # Define a senha para acessar o banco de dados
  -e DB_HOST=kube_news_db \               # Define o nome do contêiner do banco de dados como host
  --network=kube_news_net \               # Conecta o contêiner à rede Docker "kube_news_net"
  fagnerfgb/kube-news:v1                  # Nome e versão da imagem Docker do aplicativo
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

# Limpa redes não utilizadas, ou seja, redes não associadas a nenhum contêiner
docker network prune

# Limpa o cache de construção de imagens, removendo camadas que não são mais usadas
docker builder prune -a
```


