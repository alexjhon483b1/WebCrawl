#!/bin/bash

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <existing_file> <new_file>"
    exit 1
fi

# Assign the provided file names to variables
existing_file="$1"
new_links_file="$2"

# Check if the existing file exists
if [ -f "$existing_file" ]; then
    # Read existing links into an array
    mapfile -t existing_links < "$existing_file"
else
    # If the existing file doesn't exist, create an empty array
    existing_links=()
fi

# Read new links into an array
mapfile -t new_links < "$new_links_file"

# Append new links to the existing links array
for link in "${new_links[@]}"; do
    if [[ ! " ${existing_links[*]} " =~ " $link " ]]; then
        existing_links+=("$link")
    fi
done

# Write the unique links back to the existing file
printf "%s\n" "${existing_links[@]}" > "$existing_file"

echo "New links added to $existing_file"
