#!/bin/bash

read number
if (( $number > 0 ))
then
echo "$number положительное"
elif [[ $number -eq 0 ]]
then
echo "$number равно 0"
else
echo "$number отрицательное"
fi

