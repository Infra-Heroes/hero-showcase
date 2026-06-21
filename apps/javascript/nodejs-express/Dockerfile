FROM node:22-slim

WORKDIR /app

# Install express directly for the dummy example
RUN npm install express

COPY index.js .

EXPOSE 8080

CMD ["node", "index.js"]
