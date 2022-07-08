"""Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces,
and curly brackets are balanced."""
from task1 import Stack


def is_balanced(sequence) -> bool:
    match = {')': '(', ']': '[', '}': '{'}
    s = Stack([])
    for char in sequence:
        if char in '({[':
            s.push(char)
        if char in match:
            if match[char] == s.peek():
                s.pop()
            else: return False
    return True if s.is_empty() else False


print(is_balanced('[]'))
print(is_balanced('[1, 2, {3}, (), 4]'))
print(is_balanced('[], (]'))
print(is_balanced('((('))
