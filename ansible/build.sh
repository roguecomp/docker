#!/bin/bash

rm ansible/hosts
echo "[servers]" >> ansible/hosts
for num in {1..10}
do
	echo "ansible_server_$num" >> ansible/hosts
done

#building files
docker build -t ubuntu-ansible .
cd ansible;docker build -t ansible-practise .; cd ..
