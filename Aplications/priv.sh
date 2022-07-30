#!/bin/bash

if [ $(id -u) -ne 0 ]; then
  echo "como sudo webon"
  exit 1
fi

return=$(zenity --list --title="Que queri" --column="0" "another user" "searx" "tor" "matar" --width=100 --height=300 --hide-header)

if [ -z "$return" ]; then
  exit 1
fi

if [ "$return" == "another user" ]; then
  sudo -u laptop_eh bash << EOF
firefox --profile /home/laptop_eh/.mozilla/firefox/ptv87zml.aux
EOF
fi

if [ "$return" == "searx" ]; then

  localhost=http://localhost:80/
  
  pidof /usr/bin/docker-proxy
  if [ $? -ne 0 ]; then
    docker run --restart unless-stopped -d -v /home/laptop_eh/git/searx:/etc/searx -p 80:8080 -e BASE_URL=http://localhost:80/ searx/searx
  fi
  
  sudo -u laptop_eh bash << EOF
firefox --private-window $localhost --profile /home/laptop_eh/.mozilla/firefox/ptv87zml.aux
EOF

fi

if [ "$return" == "tor" ]; then
  pidof tor
  if [ $? -ne 0 ]; then
    tor &
  fi
  
  sudo -u laptop_eh bash << EOF
proxychains firefox --private-window duckduckgo.com --profile /home/laptop_eh/.mozilla/firefox/ptv87zml.aux
EOF

fi

if [ "$return" == "matar" ]; then
  docker stop $(docker container list | awk '{ print $1 }')
  killall tor
fi

