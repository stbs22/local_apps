#!/bin/bash

user_input=$(zenity --password)

if [ $? = 0 ]; then 
  echo $user_input | sudo -S $1 
else
    echo "Cancelao"
fi
