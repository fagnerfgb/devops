# Define a imagem base como Node.js na versão 22.12.0 baseada na versão alpine 3.20 (imagem leve)
FROM node:22.12.0-alpine3.20

#LABEL (Add metadata to an image)
LABEL author="Fagner Geraldes Braga"
LABEL contact="fagner.fgb@gmail.com"
LABEL description="NodeJS with Kube-News Web Application"
LABEL source="https://github.com/fagnerfgb/devops"
LABEL documentation="https://github.com/fagnerfgb/devops/blob/master/kubenews.md"

# Define o diretório de trabalho dentro do contêiner como /app
WORKDIR /app

# Copia os arquivos package.json e package-lock.json para o diretório atual no contêiner
COPY package*.json .

# Executa o comando npm install para instalar as dependências do projeto
RUN npm install

# Copia todos os arquivos do diretório atual (host) para o diretório atual no contêiner
COPY . .

# Expõe a porta 8080 do contêiner, permitindo que ela seja acessada externamente
EXPOSE 8080

# Define o comando padrão para executar quando o contêiner for iniciado
CMD [ "node", "server.js" ]
