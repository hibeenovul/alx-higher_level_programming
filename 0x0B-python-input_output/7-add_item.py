#!/usr/bin/python3
""" This module adds all arguments to a Python list, and then
save them to a file
"""

import sys
from typing import List
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("add_item.json"):
    my_list = load_file("add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)

save_file(my_list, "add_item.json")
