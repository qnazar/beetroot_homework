"""Try to use nested try catch blocks"""
a = 1
b = '0'
try:
    a / b
except Exception:
    try:
      b > 0
    except TypeError:
        print('Inner exception')
    print('Outer exception')
