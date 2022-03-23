#! /bin/bash

echo 'final: '$1
i=0
echo $i
while [ $i -ne $1 ]
do 

	sleep 1
	((i++))
	echo $i

done
