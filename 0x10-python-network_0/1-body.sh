#!/bin/bash
#This script takes in a URL, and displays the body of the response
curl -s "$1" | tr -d "\n"