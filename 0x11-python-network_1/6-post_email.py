#!/usr/bin/python3
"""
script posts val to a url passed as arg and displays response
"""
import requests
import sys

if __name__ == "__main__":
    val = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=val)
    print(r.text)
