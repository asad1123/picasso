FROM node:12.13-buster

RUN mkdir -p /usr/local/app
WORKDIR /usr/local/app

COPY public ./public
COPY src ./src
COPY package.json rollup.config.js rollup_start_dev.js rollup.preprocesses.js ./

RUN apt-get update && npm install && npm run build

EXPOSE 5000
CMD [ "npm", "run", "start" ]