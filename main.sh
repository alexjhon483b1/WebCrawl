#!/bin/bash

# Check if the domain is provided as a command-line argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

domain=$1

 ./ssl "$domain">>x.html  # Correct syntax for calling another script
 url="https://$domain"
 python3 scrap.py "$url" >> link.txt
 rm x.html
 ./curl.sh link.txt


