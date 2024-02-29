#!/bin/bash
#This script takes in URL and displays all HTTP methods the server will accept
curl -I "$1" 2>/dev/null | awk '/Allow:/ {$1=""; print substr($0,2)}'
