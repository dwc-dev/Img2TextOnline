# Img2TextOnline
一个在线图片转文字平台

## 本地部署
执行以下命令：
```bash
git clone https://github.com/dwc-dev/Img2TextOnline.git
cd Img2TextOnline
docker-compose up
```
待前后端容器启动成功后打开 http://localhost:8080

## 服务器部署

克隆项目
```bash
git clone https://github.com/dwc-dev/Img2TextOnline.git
cd Img2TextOnline
```

根据实际情况修改`docker-compose.yml`中的后端接口地址，然后执行以下命令：
```bash
docker-compose up --build -d
```
此命令将启动前端和后端容器。

推荐通过 Nginx 结合反向代理将前后端整合到一个域名下，例如：

前端：http://example.com/

后端：http://example.com/api/

反向代理配置示例（Nginx）：
```nginx
server {
    listen 80;
    
    location / {
        proxy_pass http://localhost:8080; # 前端容器
    }

    location /api/ {
        proxy_pass http://localhost:8000; # 后端容器
    }
}
```
