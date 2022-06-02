"""Write a program that searches the longest word in file"""
with open('text.txt', 'r') as file:
    data = file.read()

lst = data.split()

print(lst)

a = max(lst, key=len)
print(a)
