#! /bin/bash

# dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:org.mpris.MediaPlayer2.Player string:Metadata | sed -n '/title/{n;p}' | cut -d '"' -f 2

#total=$(playerctl metadata mpris:length)

#shit=$(playerctl metadata --format "{{ duration(position) }}" --follow)
playerctl metadata --player=spotify --format '{{ title }} - {{ artist }}' 
