"""Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
if your input is “Anton” and the stored name is “anton”, it should return True."""

name = 'nazar'
input_name = input('Enter your name: ')

if name == input_name.casefold():
    print(True)
else:
    print(False)
