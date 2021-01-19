#!/bin/bash

# synchronizing apt-get
sudo apt-get update

# installing dependencies
sudo apt install docker-compose haproxy containerd docker

# adding USER to docker group to access docker without sudo permissions
sudo usermod -a -G docker $USER
sudo systemctl restart docker
newgrp docker

./build.sh

#docker build -t my-apache .

#cd haproxy; docker build -t my-haproxy .; cd .. 
