#!/bin/bash

sudo -n java -jar /home/laptop_eh/Aplications/tlauncher/TLauncher-2.86.jar
if [ $? -ne 0 ]; then
	ask "java -jar /home/laptop_eh/Aplications/tlauncher/TLauncher-2.86.jar"
fi
