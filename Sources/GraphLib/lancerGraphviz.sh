#!/bin/bash

for fileName in `ls *.dot`
do
	imageName=`echo $fileName".jpg"`
	#echo $imageName
	#echo $fileName

	dot -Tjpeg -o $imageName $fileName
done
