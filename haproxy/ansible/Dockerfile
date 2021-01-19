FROM centos:latest

RUN yum install epel-release -y
RUN yum update -y 
RUN yum install ansible -y
RUN yum install -y python3
COPY hosts /etc/ansible/hosts
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh
RUN dnf install -y openssh-server openssh-clients
RUN echo 'root:root' | chpasswd
EXPOSE 22

COPY sshd_config /etc/ssh/sshd_config

