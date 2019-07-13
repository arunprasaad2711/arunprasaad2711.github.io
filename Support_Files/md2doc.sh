#!/bin/bash
# This file lists down all the md files in a directory 
# and merges it into a docfile file.

pandoc -s -o doc.docx *.md
pandoc -s -o doc.html *.md
