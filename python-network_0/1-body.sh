#!/bin/bash
# Sends a GET request to a URL and displays the body only if the status is 200
response=$(curl -s -w "%{http_code}" "$1"); [ "${response: -3}" = "200" ] && echo "${response%???}"
