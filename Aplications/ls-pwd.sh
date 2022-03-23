#!/usr/bin/env bash

if [[ -z $1 ]]
then
	echo "Sin argumento"
else
	echo $(pwd -P)/$(ls $1)
fi