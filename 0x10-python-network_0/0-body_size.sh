#!/bin/bash


#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract URL from argument
url=$1

# Send request to the URL and save the response body to a temporary file
response=$(curl -s -o temp_response.txt -w "%{size_download}" "$url")

# Check if curl command was successful
if [ $? -eq 0 ]; then
    # Display the size of the response body in bytes
    echo "Size of response body: $response bytes"
else
    echo "Failed to retrieve response from the URL: $url"
fi

# Clean up temporary file
rm -f temp_response.txt

