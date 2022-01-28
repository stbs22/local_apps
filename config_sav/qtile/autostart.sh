#!/bin/sh

rclone --vfs-cache-mode writes mount 'GDrive_eh': ~/Drive_eh &
rclone --vfs-cache-mode writes mount 'GDrive_GB': ~/Drive_gb &
rclone --vfs-cache-mode writes mount 'OneDrive UAI': ~/OneDrive &

picom &
flameshot &
feh --bg-fill --randomize ~/Imágenes/wallp &
xscreensaver -no-splash &
start-pulseaudio-x11 &

numlockx on &
volumeicon &
blueman-applet &
nm-applet &
