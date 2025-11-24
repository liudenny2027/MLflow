FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 避免生成pyc文件并让输出更及时
ENV PYTHONUNBUFFERED=1

# 复制 requirements 并安装依赖
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 复制项目源代码
COPY . /app

# 使入口脚本可执行
RUN chmod +x /app/start.sh

# MLflow UI 默认端口
EXPOSE 5000

# 启动容器时运行脚本：先训练，再启动 MLflow UI
CMD ["/bin/sh", "/app/start.sh"]
