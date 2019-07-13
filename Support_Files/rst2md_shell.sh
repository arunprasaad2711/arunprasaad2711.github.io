#!/bin/bash
# This file lists down all the rst files in a directory 
# and converts it into a markdown file.

FILES=*.rst
for f in $FILES
do
  filename="${f%.*}"
  echo "Converting $f to $filename.md"
  `pandoc $f -f rst -t markdown -o $filename.md`
done
