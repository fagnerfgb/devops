FROM cgr.dev/chainguard/node
ENV NODE_ENV=production
WORKDIR /app
COPY --chown=node:node package*.json ./
RUN npm install --omit-dev
COPY --chown=node:node . .
EXPOSE 8080
CMD ["server.js"]