#!/bin/bash

filelist=`ls /storage/chem/msrgxt/dcd_files`
for file in $filelist
do
	./convert "/storage/chem/msrgxt/dcd_files/$file" "/storage/chem/msrgxt/exyz_files/$file.xyz"
	echo "$file is done."
done

