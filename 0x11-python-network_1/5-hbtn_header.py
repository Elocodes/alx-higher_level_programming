#!/usr/bin/python3
"""
script fetches a url passed as arg and displays the value of
the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
