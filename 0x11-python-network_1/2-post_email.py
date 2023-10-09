#!/usr/bin/python3
"""
script sends post request to url passed as arg, displays the
body of the response decoded in utf-8
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email_address = sys.argv[2]
    value = {"email": email_address}

    data = urlencode(value).encode('ascii')
    req_val = Request(url, data)

    with urlopen(req_val) as response:
        print(response.read().decode('utf-8'))
