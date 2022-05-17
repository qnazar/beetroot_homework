# Write a Python program that accepts a string of numbers and find the smallest number

string = input('Enter the string of digits: ')
smallest = 9
for i in string:
    if i.isdigit() and int(i) < smallest:
        smallest = int(i)
print(smallest)
# ------------------------------ #
list_of_digits = []
for i in string:
    if i.isdigit():
        list_of_digits.append(int(i))
print(min(list_of_digits))
