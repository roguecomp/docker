#!/bin/bash

ssh-keygen -f /root/.ssh/id_rsa -P ""
for num in {1..10}
do
	ssh-copy-id ansible_server_$num
done
exit 0
