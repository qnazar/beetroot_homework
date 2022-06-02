"""Write a Python program that read file and to removes newline characters"""

with open('text.txt', 'r') as file:
    data = file.readlines()

new = []
for line in data:
    new.append(line.rstrip('\n'))

print(new)
