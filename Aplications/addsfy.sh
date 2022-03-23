#!/usr/bin/env bash

killall spotify
sleep 3
spotify
sleep 5
playerctl play-pause

notify-send "Recordar sesión privada"
