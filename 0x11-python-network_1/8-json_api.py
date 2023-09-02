#!/usr/bin/python3
"""
script posts val to a url passed as arg and displays a valid json response
"""
import requests
import sys

if __name__ == "__main__":
    val = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=val)
    try:
        content = r.json()
        if not content:         #no content, json empty
            print('No result')
        else:
            print('[{}] {}'.format(content.get('id'), content.get('name')))
    except ValueError:
        print('Not a valid JSON')
