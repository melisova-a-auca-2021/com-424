#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Usage: $0 <filename> <word>"
    exit 1
fi

file=$1
word=$2

if [ ! -f "$file" ]; then
    echo "File not found!"
    exit 1
fi

count=$(grep -o -i "$word" "$file" | wc -l)

echo "The word '$word' appears $count times in $file."
