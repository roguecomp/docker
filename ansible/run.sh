#!/bin/bash

echo "---------------------------------------------------------"
echo "--------------[Docker Creating containers]---------------" 
echo "---------------------------------------------------------"
docker-compose up --no-start

echo ""
echo "---------------------------------------------------------"
echo "--------------[Docker Starting containers]---------------"
echo "---------------------------------------------------------"
docker-compose start

echo ""
echo "---------------------------------------------------------"
echo "---------------[switching on ssh server]-----------------"
echo "---------------------------------------------------------"

for num in {1..10}
do
	echo "server number $num: "
	docker exec -it ansible_server_$num service ssh start
	echo ""
done

docker exec -it ansible bash
