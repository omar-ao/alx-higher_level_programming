#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and displays the"""

import urllib.request
import sys


url = sys.argv[1]
req = urllib.request.Request(url)


if __name__ == '__main__':
    with urllib.request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))
