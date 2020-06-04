#!/usr/bin/python3
"""This module load data from JSON files
an save arguments into a JSON file
"""
from sys import argv

save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file
try:
    data_list = load("add_item.json")
except:
    data_list = []
data_list.extend(argv[1:])
save(data_list, "add_item.json")
