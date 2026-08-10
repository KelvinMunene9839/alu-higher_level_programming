#!/usr/bin/python3
"""Prints the X-Request-Id header value of a URL's response."""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
