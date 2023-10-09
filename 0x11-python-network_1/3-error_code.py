#!/usr/bin/python3
"""
script sends post request to url passed as arg, displays the
body of the response decoded in utf-8, and manages httperror
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
