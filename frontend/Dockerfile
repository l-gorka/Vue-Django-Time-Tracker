FROM node:lts-alpine

WORKDIR /app/frontend/

COPY package.json .
COPY package-lock.json .

RUN npm ci


EXPOSE 8080
