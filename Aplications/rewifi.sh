#!/bin/bash

#wifi supplicant
notify-send -t 1000 -u low "Sending"

wget -q --tries=10 --timeout=20 --spider http://google.com
if [[ $? -eq 0 ]]; then
        notify-send -t 1000 -u normal "Online"
else
        notify-send -t 1000 -u critical "Offline"
			
		for SSID in "Vet I" "UAI Alumnos" "iPhone de Esteban";
		do     
			nmcli d wifi connect "$SSID"
			
			if [[ $? -eq 0 ]]; then
				notify-send -t 1500 -u normal "Conectado a $SSID"
				exit 1
			fi
		
		done

		notify-send -t 1500 -u critical "Fallo en Conexión"
fi
