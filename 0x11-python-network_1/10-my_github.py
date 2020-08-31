#!/usr/bin/python3
""" My Github
    This module holds a Python script that takes your Github
    credentials (username and password) and uses the Github API
    to display your id use the package requests and sys
"""
import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get("id"))
