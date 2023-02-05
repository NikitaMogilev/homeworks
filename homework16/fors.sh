#!/bin/bash


evennum=""
for (( i=1; i<=11; i++ ))
do
remainder=$(( $i % 2 ))
if [ $remainder -eq 0 ]; then
evennum="$evennum $i "
fi
done
echo "Even numbers are: "$evennum


