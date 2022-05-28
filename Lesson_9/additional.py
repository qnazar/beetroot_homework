"""Create a program that sums all user-entered numbers while ignoring any rows of invalid numbers entered by the user.
Your program should display the current total as each number is entered.
It should display an appropriate error message after each invalid input,
then aggregate any other numbers the user entered. When the user enters a blank line, your program should exit.
Make sure your program works correctly for both integers and floats counting"""

suma = 0
while True:
    number = input('Enter the number to sum: ').strip()
    if number == '':
        print('Good bye')
        break
    try:
        number = float(number)
    except ValueError:
        print('I can\'t add this type of symbols')
        continue
    suma += number
    print('Current total is', suma)


x = [lambda x,y: x+y for x in range(5) for y in range(5)]
print(x)

