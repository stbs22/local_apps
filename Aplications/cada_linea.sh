#!/bin/bash
echo Leyendo

i=27
sleep 1
cat $1 | while read line
do
  echo "Descargando Clase $i"
  youtube-dl $line -o ~/Vídeos/ECO/ECO_clase_$i
  sleep 10
  echo "Ejecucion"
  let i=$i+1
done
