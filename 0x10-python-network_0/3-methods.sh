#!/bin/bash
#This script takes in URL and displays all HTTP methods the server will accept
curl -X OPTIONS "$1" 
