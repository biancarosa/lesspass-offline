FROM node:lts AS builder
LABEL maintainer="Bianca Rosa <me@biancarosa.com.br>"
LABEL name="LessPass Pure Offline Frontend" 
WORKDIR /opt/frontend
COPY /lesspass/packages/lesspass-pure ./
RUN npm install -g gulp @vue/cli @vue/cli-service @vue/cli-service-global
RUN yarn install
COPY . /opt/frontend
RUN yarn build
FROM nginx:alpine
COPY --from=builder /opt/frontend/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]