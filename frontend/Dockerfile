# 构建阶段
FROM node:16 AS build

WORKDIR /app

# 拷贝项目依赖文件
COPY package.json yarn.lock ./
RUN yarn install

# 拷贝项目文件
COPY . .

# 使用构建参数替换 .env 文件中 VUE_APP_API_URL 的值
ARG VUE_APP_API_URL
RUN sed -i "s|^VUE_APP_API_URL=.*|VUE_APP_API_URL=${VUE_APP_API_URL}|" .env

# 构建前端项目
RUN yarn build

# 运行阶段
FROM nginx:alpine
WORKDIR /usr/share/nginx/html

# 将构建好的静态文件复制到 Nginx 容器
COPY --from=build /app/dist .

# 拷贝自定义 Nginx 配置文件
# COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
