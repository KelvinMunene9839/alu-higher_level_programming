#!/bin/bash
# Follows redirects, sends a GET request, and displays the body if status is 200
response=$(curl -s -L -w "%{http_code}" "$1"); [ "${response: -3}" = "200" ] && printf '%s' "${response%???}"
