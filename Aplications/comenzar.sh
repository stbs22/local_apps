#!/bin/bash
if [ -z $2 ]; then
	notify-send -t 1000 -u low "Abriendo $1"
	$1
else
	notify-send -t 1000 -u low "Abriendo $2"
	$1
fi
