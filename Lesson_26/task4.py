"""Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
Any other element must remain in the queue respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message"""


class Queue:
    def __init__(self, items):
        self.items = items

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        return self.items.pop()

    def get_from_queue(self, value):
        for i, val in enumerate(self.items):
            if val == value:
                return self.items.pop(i)
        else:
            raise ValueError('No such value in this stack')

    def __repr__(self):
        return f'Queue: -> {self.items} ->'


q = Queue([1, 2, 3, 4, 5])
print(q)
q.dequeue()
print(q)
q.enqueue(0)
print(q)
value = q.get_from_queue(2)
print('Value: ', value)
print(q)
