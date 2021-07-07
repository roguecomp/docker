FROM ubuntu:latest

RUN apt update && \
apt install -y ansible python3
COPY hosts /etc/ansible/hosts
COPY startup.sh /startup.sh
RUN chmod +x startup.sh && \ 
apt install -y openssh-server sshpass
EXPOSE 22

