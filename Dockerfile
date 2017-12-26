FROM python:latest

RUN install Flask==0.12.2 requests==2.18.4

ADD . /app

WORKDIR /app

CMD ["python", "/app/blockchain.py"]
