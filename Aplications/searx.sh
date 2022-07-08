#!/bin/bash

localhost=http://localhost:80/

export PORT=80

sudo docker run --rm -d -v /home/laptop_eh/git/searx:/etc/searx -p $PORT:8080 -e BASE_URL=http://localhost:$PORT/ searx/searx

firefox --private-window localhost:80
