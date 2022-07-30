#!/bin/bash


sudo -n $1

if [ $? -ne 0 ]; then

	user_input=$(zenity --password )
	
  echo "input success"

	if [ $? -eq 0 ]; then 
   
    echo check
		
    echo $user_input | sudo -S $1 
	  
    echo "--->$?"	
		if [ $? -ne 0 ]; then
			echo "Bad req"
      notify-send -t 2000 -u critical "ta malo webon"
			exit 1
		fi

	else
		echo "Cancelao"
		exit 1
	fi
fi
