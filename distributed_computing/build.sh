#!/bin/bash

rm ansible/hosts
echo "[servers]" >> ansible/hosts
for num in {1..10}
do
	echo "ansible_server_$num" >> ansible/hosts
	echo "ansible_server_$num" >> src/machinefile
done

echo "" >> ansible/hosts
echo "[servers:vars]" >> ansible/hosts
echo "ansible_ssh_user=root" >> ansible/hosts
echo "ansible_ssh_pass=root" >> ansible/hosts
echo "ansible_ssh_extra_args='-o StrictHostKeyChecking=no'" >> ansible/hosts
