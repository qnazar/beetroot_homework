"""Implement a stack using a singly linked list."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        current = self.head
        self.head = self.head.next_node
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


s = Stack()
s.push(2)
s.push(5)
s.push(8)
s.push(7)

print(s)

print(s.pop())
print(s)

print(s.size())
