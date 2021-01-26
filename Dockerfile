FROM ubuntu:latest

RUN apt update && apt upgrade -y \
 apt install python3.8 python3-cryptography uvicorn python3-pip

COPY ctc /app

CMD []

EXPOSE 80