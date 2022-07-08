"""Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order. Consider the case in which the element is not found -
 raise ValueError with proper info Message"""
from task1 import Stack


class ExtendedStack(Stack):

    def get_from_stack(self, value):
        for i, val in enumerate(self.items):
            if val == value:
                return self.items.pop(i)
        else:
            raise ValueError('No such value in this stack')


es = ExtendedStack([1, 2, 3, 4, 5])
print(es.get_from_stack(2))
print(es)
