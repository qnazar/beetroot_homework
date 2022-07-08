"""Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack."""


class Stack:

    def __init__(self, items):
        self.items = items

    def is_empty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def reverse(self):
        rev = []
        while not self.is_empty():
            rev.append(self.pop())
        return rev

    def __repr__(self):
        return f'<Stack> {self.items}'


def reverse(seq):
    s = Stack(seq)
    while not s.is_empty():
        print(s.pop(), end=' ')


if __name__ == '__main__':
    reverse([1, 2, 3, 4, 5])
