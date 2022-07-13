"""Implement a queue using a singly linked list."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def dequeue(self):
        current = self.head
        previous = None
        while current.next_node:
            previous = current
            current = current.next_node
        if previous:
            previous.next_node = None
        else:
            self.head = None
        return current.data

    def is_empty(self):
        return True if not self.head else False

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def __repr__(self):
        res = ''
        current = self.head
        while current:
            res += str(current.data) + ' -> '
            current = current.next_node
        return res


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q)
