#!/usr/bin/python3
"""
script sends request to url passed as arg, displays the value of the
"X-Request-Id" found in the header
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        print("{}".format(res.headers["X-Request-Id"]))
