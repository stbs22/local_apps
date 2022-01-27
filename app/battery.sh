#!/bin/bash

if [[ -n $(pidof picom) ]]

then

  killall picom
  killall blueman-applet
  sleep 1
  xfwm4 --compositor=on -r

else
  
  xfwm4 --compositor=off -r
  sleep 1
  $(picom)
  $(blueman-applet)

fi
