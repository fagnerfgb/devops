FROM node:22.13.0-alpine3.21
USER node
WORKDIR /app
COPY --chown=node:node package*.json .
RUN npm install
COPY --chown=node:node . .
EXPOSE 8080
CMD [ "node", "server.js" ]
