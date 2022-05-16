nombre=$(zenity --entry \
                --width=400 \
                --ok-label="Buscar" \
                --text="Buscar en Google")
if [[ $? -eq 0 ]]
then
	firefox --search "$nombre"
fi
