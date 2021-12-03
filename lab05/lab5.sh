#!/bin/bash
ps -eo ruid,euid,cmd | while read txt
do
	row=($txt)
	if [ ${row[0]} != ${row[1]} ]; then
		echo "${row[2]}"
	fi
done
