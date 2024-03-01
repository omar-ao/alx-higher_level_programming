#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    print("Body response:")
    print("    - type: {}".format(type(data)))
    print("    - content: {}".format(data))
    print("    - utf8 content: {}".format(data.decode('utf8')))
