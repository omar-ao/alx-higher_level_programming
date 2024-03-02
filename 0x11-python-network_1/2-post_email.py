#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

data = {}
data['email'] = sys.argv[2]
data = urllib.parse.urlencode(data).encode('utf-8')
with urllib.request.urlopen(sys.argv[1], data) as response:
    print(response.read().decode('utf-i'))
