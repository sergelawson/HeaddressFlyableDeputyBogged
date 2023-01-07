FROM node:16 AS backend

WORKDIR /app/serve

ADD package.json .
ADD yarn.lock .
ADD tsconfig.json .

RUN yarn install

ADD . .

RUN yarn build

EXPOSE 8080

# docker build -t expressapi:postgis .

# docker run -d -p 8080:8080 --name expressapp --rm expressapi:postgis

CMD ["yarn", "start"]


# docker network create app-network