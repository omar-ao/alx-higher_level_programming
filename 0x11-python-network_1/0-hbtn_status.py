#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('utf8')))
