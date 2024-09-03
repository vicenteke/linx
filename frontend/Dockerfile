FROM node:14-alpine as base

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json

RUN apk add --no-cache bash
RUN npm install --force
RUN npm install react-scripts@latest -g

COPY . /app/


############################## Devel stage ##############################
FROM base as devel

EXPOSE 3000

CMD ["/bin/bash", "-c", "npm start"]
