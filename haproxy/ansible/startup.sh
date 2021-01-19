#!/bin/bash

ssh-keygen -f /root/.ssh/id_rsa -P ""
ssh-copy-id website1
ssh-copy-id website2
ssh-copy-id website3
ssh-copy-id website4
ssh-copy-id haproxy

