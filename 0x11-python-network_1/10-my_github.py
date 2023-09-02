#!/usr/bin/python3
"""
script takes github username and passwrd passed as args and uses the
github API to display id
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        content = r.json()
        print(content.get('id'))
    except ValueError:
        print('Not a valid JSON')
