# 使用 Python 3.12 基础镜像
FROM python:3.12-slim

# 安装必要的工具
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 设置python镜像源（可选）
ENV PIP_INDEX_URL=https://mirror.sjtu.edu.cn/pypi/web/simple

# 设置时区
ENV TZ=Asia/Shanghai

# 安装 Python 依赖
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 复制代码文件
COPY app.py /app/

# 暴露端口 8000
EXPOSE 8000

# 设置容器入口
ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:8000", "--wsgi-file", "app.py", "--callable", "app", "--processes", "4", "--threads", "2"]
