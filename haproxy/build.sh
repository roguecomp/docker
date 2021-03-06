#!/bin/bash

echo "--------------------------[Building Docker my-apache Image]---------------------------"
cd apache2; docker build -t my-apache .; cd ..

echo "--------------------------[Building Docker my-haproxy Image]--------------------------"
cd haproxy; docker build -t my-haproxy .; cd ..
