#!/usr/bin/python3
""" Response header value #0
    This module holds a Python script hat takes in a URL,
    sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response
    using the packages urllib and sys
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
