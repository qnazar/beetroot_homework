"""Create your own defined exception with custom message
(if can be devision by 0 or value error)."""

try:
    1/0
except ZeroDivisionError:
    print('Your math teacher: "You\'re such a bastard"')

