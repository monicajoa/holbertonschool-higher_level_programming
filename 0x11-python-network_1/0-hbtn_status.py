#!/usr/bin/python3
""" What's my status? #0
        This module holds a Python script that fetches
        https://intranet.hbtn.io/status, using the package urllib
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
