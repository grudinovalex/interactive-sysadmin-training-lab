FROM node:latest

LABEL maintainer="grudinov.alex@gmail.com"

SHELL ["/bin/bash", "-c"]

RUN npm i -g wetty@2.6.0 && \
apt -y update && \
apt -y install sshpass

EXPOSE 3000

ENTRYPOINT ["wetty", "--ssh-host=istl", "--ssh-port=22", "--ssh-user='trainee'", "--ssh-pass='istl2024'", "--allow-iframe"]
