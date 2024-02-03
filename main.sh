#!/bin/bash

# Check if the domain is provided as a command-line argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

domain=$1

# Run your program with the provided domain and capture the output
output=$(./checkssl "$domain" 2) 

# Get the last line using awk
last_line=$(echo "$output")

# Now you can check or use the last line as needed
echo "$last_line"

if [ "$last_line" = "HTTPS" ]; then
 ./ssl "$domain">>x.html  # Correct syntax for calling another script
 url="https://$domain"
 python3 scrap.py "$url"
 rm x.html
fi

if [ "$last_line" = "HTTP" ]; then
 get=$(./get "$domain")>>x.html  # Correct syntax for calling another script
 url="https://$domain"
 python3 scrap.py "$url"
 rm x.html
fi

