#!/bin/bash

rm ansible/hosts
echo "[webservers]" >> ansible/hosts
for num in {1..10}
do
	echo "ansible_$num" >> ansible/hosts
done

#building files
docker build -t ubuntu-ansible .
cd ansible;docker build -t ansible-practise .; cd ..
