#! /bin/bash
#de inicio a final

val= $(playerctl metadata mpris:length) / 1000000
echo 1. $val
j=$(date | awk '{print substr($5,7,8)}')
echo 2. $j
val=$(($val - $j))
echo 3. $val


