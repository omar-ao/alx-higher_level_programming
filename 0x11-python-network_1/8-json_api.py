#!/usr/bin/python3
"""
This script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if len(sys.argv) == 2:
        q = sys.argv[1]

    r = requests.post(url, data={'q': q})
    if 'application/json' in r.headers.values():
        result = r.json()
        if result:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
