#!/usr/bin/python3
"""
This script that takes 2 arguments repository name and owner name
and lists 10 commits (from the most recent to oldest) of the repository

Usage:
    ./100-github_commits.py <ropository name> <owner name>
"""
import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)
    r = requests.get(url)
    commits = r.json()
    newest = commits[-10:]
    for commit in newest:
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, name))
