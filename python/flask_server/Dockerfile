FROM python:3.7.3-alpine3.9

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

WORKDIR /app

COPY src /app/src

CMD python3 /app/src/main.py

