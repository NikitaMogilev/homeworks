#!/bin/bash 

PS3="Хотите ли Вы установить python?”"
echo
select choice in "Yes" "No"
do
case $choice in
"Yes")echo "Вы выбрали установить python";;
"No") echo "Уходи дверь закрой";;
esac && break
done 

