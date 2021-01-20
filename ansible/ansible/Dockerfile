FROM centos:latest

RUN yum install epel-release -y && \
yum update -y && \
yum install ansible -y && \
yum install -y python3
COPY hosts /etc/ansible/hosts
COPY startup.sh /startup.sh
RUN chmod +x startup.sh && \ 
dnf install -y openssh-server openssh-clients
EXPOSE 22

