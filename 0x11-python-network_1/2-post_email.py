#!/usr/bin/python3
"""
This script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)

Usage:
    ./2-post_email.py <url> <email>
"""

import urllib.request
import sys


if __name__ == '__main__':
    data = {}
    data['email'] = sys.argv[2]
    data = urllib.parse.urlencode(data).encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-i'))
