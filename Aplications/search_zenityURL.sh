nombre=$(zenity --entry \
                --width=400 \
                --ok-label="Buscar" \
                --text="Buscar URL")
if [[ $? -eq 0 ]]
then
	firefox --new-window "$nombre"
fi
