"""Write a Python program to create a new JSON file from an existing JSON file."""
import json

# data = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
#
# with open('test.json', 'w') as file:
#     json.dump(data, file)

with open('test.json', 'r') as file:
    data = json.load(file)

with open('new.json', 'w') as file:
    json.dump(data, file,indent=4)
