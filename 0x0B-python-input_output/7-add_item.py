#!/usr/bin/python3
"""Script that adds all arguments to a Python list
and then save them to a file
"""


import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


items = []
if os.path.isfile("add_item.json"):
    json_item = load_from_json_file("add_item.json")
    for item in json_item:
        items.append(item)

for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])

save_to_json_file(items, "add_item.json")
