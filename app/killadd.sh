#! /bin/bash
killall spotify
sleep 2

xdotool key alt+KP_5
sleep 0.1
xdotool key 0xff7f

sleep 0.1
spotify
