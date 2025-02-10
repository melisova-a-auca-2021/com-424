#!/bin/bash

# Check if exactly one argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Assign the argument to a variable
dir=$1

# Check if the provided argument is a valid directory
if [ ! -d "$dir" ]; then
    echo "Error: Directory '$dir' not found!"
    exit 1
fi

# Find and delete empty files, while printing their names
find "$dir" -type f -empty -print -delete

echo "All empty files in '$dir' have been deleted."
