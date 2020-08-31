#!/usr/bin/python3
""" Search API
    This module holds a Python script that takes in a letter
    and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter, using  the package requests and sys
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}
    response = requests.post(url, data=values)
    try:
        json_r = response.json()
        if json_r:
            print("[{}] {}".format(json_r['id'], json_r['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
