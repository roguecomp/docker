# apache2-website with docker containers and haproxy

Dependencies:
	docker
	docker-compose

Running dependencies.sh:
1) sudo chmod +x dependencies.sh
2) ./dependencies.sh
3) no restart needed

Run Instructions:
1) Put source code inside website folder (main file index.html).
2) ./build.sh
3) ./run.sh (creates and starts containers and puts you in maintainence vm {ansible}) 

you can now visit website on 127.0.0.1:8080. or http://(YOUR IP):8080
