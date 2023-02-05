#!/bin/bash

read sumbol
case $sumbol in
[[:lower:]]) echo " нижнем регистре";;
[[:upper:]]) echo " в верхнем регистре";;
[0-9]) echo " для проверки на число";;
esac 
