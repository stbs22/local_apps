#!/bin/bash

#wifi supplicant
notify-send -t 1000 -u low "Revisando crack"

ping 8.8.8.8 -c 3 -W 3
if [[ $? -eq 0 ]]; then
       	notify-send -t 4000 -u normal "Conectado en:" "$(nmcli -t -f TYPE c show --active)"
else
        notify-send -t 1000 -u critical "Fuera de Linea" "Intentando Reconectar"
			
		for SSID in "Vet I" "UAI Alumnos" "iPhone de Esteban";
		do     
			nmcli con down "$SSID 1"
			sleep 1;
			nmcli d wifi connect "$SSID"	
			if [[ $? -eq 0 ]]; then
				notify-send -t 1500 -u normal "Devuelta en Linea para $SSID"
				exit 1
			else
			  	notify-send -t 1000 -u critical "Error para $SSID"
			fi
		
		done

		notify-send -t 1500 -u critical "Fallo en Conexión"
fi
