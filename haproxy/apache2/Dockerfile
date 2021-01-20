FROM httpd:latest
COPY httpd.conf /usr/local/apache2/conf/httpd.conf 
COPY website /usr/local/apache2/htdocs/
RUN apt update && apt install -y curl 

