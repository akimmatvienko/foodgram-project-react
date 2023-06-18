# build env
FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
RUN NODE_ENV=development npm i
RUN npm audit fix
CMD cp -r build result_build
