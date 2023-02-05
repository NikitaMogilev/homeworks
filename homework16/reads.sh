#!/bin/bash

read number

if (( $number > 15 & $number <45 ))
then 
echo "$number число в интервале от 15 до 45"
else
echo "$number число не из диапазона от 15 до 45"
fi
