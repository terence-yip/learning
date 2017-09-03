FROM debian:8.9

WORKDIR /app

RUN apt-get update && apt-get install -y vim

RUN apt-get install -y python3

COPY simple_server /app/simple_server

EXPOSE 80

CMD python3 /app/simple_server/main.py
