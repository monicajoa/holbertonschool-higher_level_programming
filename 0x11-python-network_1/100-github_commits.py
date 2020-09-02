#!/usr/bin/python3
""" Time for an interview
    This module holds a Python script that takes 2
    arguments in order to solve this challenge
    The first argument will be the repository name
    The second argument will be the owner name
    using the packages requests and sys
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    for i in response.json()[0:10]:
        print("{}: {}".format(i.get('sha'), i.get(
            'commit').get('author').get('name')))
