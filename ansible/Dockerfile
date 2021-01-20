FROM ubuntu:latest

RUN apt update && \ 
apt install -y python3 openssh-server && \
echo 'root:root' | chpasswd

EXPOSE 22

COPY sshd_config /etc/ssh/sshd_config
