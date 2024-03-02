#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter,
and finally displays the body of the response.

Usage:
    ./6-post_email.py <url> <email>
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)
