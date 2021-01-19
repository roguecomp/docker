FROM haproxy:latest

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
RUN apt update && apt install -y curl
RUN apt install -y python3 openssh-server
RUN echo 'root:root' | chpasswd
EXPOSE 22

COPY sshd_config /etc/ssh/sshd_config
