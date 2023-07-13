# build stage
FROM node:20.4.0 as build-stage
WORKDIR /app
COPY frontend/package*.json ./
RUN yarn install
COPY frontend .
RUN yarn run build

# production stage
FROM nginx:1.25.1 as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]