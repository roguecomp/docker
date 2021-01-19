FROM httpd:latest
COPY httpd.conf /usr/local/apache2/conf/httpd.conf 
COPY website /usr/local/apache2/htdocs/
RUN apt update && apt install -y curl
RUN apt install -y openssh-server python3
RUN echo 'root:root' | chpasswd

EXPOSE 22

COPY sshd_config /etc/ssh/sshd_config
