#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Required one argument!"
	exit 1
fi

echo "Connecting to $1"

ping -c 4 $1 &> /dev/null

if [ $? -ne 0 ]; then
	echo "Couldn't reach the site"
	exit 1
else
	echo "Ok"
	exit 0
fi
