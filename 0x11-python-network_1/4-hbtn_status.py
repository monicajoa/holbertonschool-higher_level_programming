#!/usr/bin/python3
""" What's my status? #1
    This module holds a Python script that
    fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
