# Create a string. Replace special symbols in your string with #.
# Example: input = “&^hwjys*%#” output = “##hwjys###”

string = '&^hwj ys*%#'
for char in string:
    if not char.isalnum() and not char.isspace():
        string = string.replace(char, '#')
print(string)


