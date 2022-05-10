# Create two strings and check if all the characters in the string1 are present in string2
# and print the result (True or False)

string1 = 'check'
string2 = 'Do your homework properly'

result = None
for char in string1:
    if char not in string2:
        result = False
        break
    else:
        result = True

print(result)
