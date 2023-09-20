FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /app

RUN apt update && apt install gcc build-essential libpq-dev -y

RUN pip install wheel

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["./start.sh"]
