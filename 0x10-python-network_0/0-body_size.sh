#!/bin/bash
#This script takes in a URL, sends a request to that URL, and displays the size
curl -w '%{size_download}' "$1" -so /dev/null ; echo 
