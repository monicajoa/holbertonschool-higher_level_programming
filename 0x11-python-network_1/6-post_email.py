#!/usr/bin/python3
""" POST an email #1
    This module holds a Python script that takes in a URL
    and an email address, sends a POST request to the passed
    URL with the email as a parameter, and finally displays
    the body of the response, using the packages requests and sys
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    response = requests.post(url, data=values)
    print(response.text)
