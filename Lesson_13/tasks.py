# 1. Convert the following function to a lambda expression and assign it to a variable called exp.
def exponentiate(base, exponent):
    return base ** exponent

exp = lambda a, b: a ** b
print(exp(5, 2))

# 2. Create a list of dictionaries with name, surname and age of each person.
# Write a python program using lambda function to sort the order of names based on its alphabet sequence.
# Write another program to sort by age. Write result to JSON file.

my_list = [{'name': "Nazar", 'surname': 'Klypych', 'age': 26},
           {'name': 'Ira', 'surname': 'Cher', 'age': 24},
           {'name': 'Danya', 'surname': 'Martiuk', 'age': 14}]


by_name = sorted(my_list, key=lambda x: x['name'])
print(by_name)
by_age = sorted(my_list, key=lambda x: x['age'])
print(by_age)
for i in by_name:
    print(i['name'])


# 3. Write a python program to generate a lambda function to check whether a given string is a number or not. (True or False)

check = lambda x: x.replace('.', '').isdigit()
test = '123.5'
print(check(test))


# 4. Find the errors in this code:
def fun1(a):
    x = a * 3
    def fun2(b):
      return b + x
    return fun2
test_fun = fun1(4)
print(test_fun(7))
# Result: 19

# 5. Write a quadratic quadratic equation, pass the a, b, c, and x to solve it. For example: f1 = make_quadratic(1, 0, 0)
# f1(5)
# Result 25
# ax**x + bx + c = 0


def make_quadratic(a, b, c):
    def solve_it(x):
        return a * x**2 + b*x + c
    return solve_it


f1 = make_quadratic(1, 0, 0)
result = f1(5)
print(result)


# 6. Use map() function to print the square of each numbers rounded to 2 decimals
my_floats = [42.35, 68.09, 1.25, 9.77, 1.16, 5.88, 90.59]
result = list(map(lambda x: round(x ** 2, 2), my_floats))
print(result)


# 7. Use filter to print only the names that are less than or equal to 10 letters
names = ['kdjeg', 'kskdff;m;', 'weockm', 'ajeiedsnjcsd', 'dhgc', 'jebenajdlkncfg']
result = list(filter(lambda x: len(x) <= 10, names))
print(result)


# 8. Use reduce to print the product of these numbers
from functools import reduce
my_numbers = [3, 6, 90, 23, 10]
result = reduce(lambda x, y: x * y, my_numbers)
print(result)
