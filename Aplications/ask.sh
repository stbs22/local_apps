#!/bin/bash


sudo -n $1

if [ $? -ne 0 ]; then

	user_input=$(zenity --password )
	
	if [ $? -eq 0 ]; then 

		echo $user_input | sudo -S $1 
		
		if [ $? -ne 0 ]; then
			notify-send -t 2000 -u critical "ta malo webon"
			exit 1
		fi

	else
		echo "Cancelao"
		exit 1
	fi
fi
