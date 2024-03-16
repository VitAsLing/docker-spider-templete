FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到位于/app中的容器中
COPY . /app

ENV PYTHONPATH /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./src/main.py"]