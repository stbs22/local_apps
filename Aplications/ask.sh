#!/bin/bash

user_input=$(zenity --password )

if [ $? -eq 0 ]; then 

	echo $user_input | sudo -S $1 
	
	if [ $? -ne 0 ]; then
		notify-send -t 2000 -u critical "ta malo webon"
	fi

else
    echo "Cancelao"
fi
