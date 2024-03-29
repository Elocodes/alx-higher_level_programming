#!/usr/bin/python3
"""
script fetches a url using requests
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.url)))
    print("\t- content: {}".format(r.text))
