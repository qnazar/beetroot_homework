"""Extend UnorderedList
Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two
parameters `start` and `stop`, and return a copy of the list starting at the position
and going up to but not including the stop position."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class UnorderedLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == data:
                found = True
                if previous:
                    previous.next_node = current.next_node
                else:
                    self.head = current.next_node
            else:
                previous = current
                current = current.next_node

    def is_empty(self):
        return True if not self.head else False

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def append(self, data):
        current = self.head
        while current.next_node:
            current = current.next_node
        new_node = Node(data)
        current.next_node = new_node

    def index(self, data):
        current = self.head
        count = 0
        while current:
            if current.data == data:
                return count
            else:
                current = current.next_node
                count += 1
        else: return None

    def pop(self, pos=None):
        current = self.head
        if pos is None:
            while current.next_node:
                current = current.next_node
            self.remove(current.data)
            return current.data
        else:
            count = 0
            while count != pos:
                current = current.next_node
                count += 1
            self.remove(current.data)
            return current.data

    def insert(self, pos, data):
        if pos == 0:
            self.add(data)
        else:
            new_node = Node(data)
            current = self.head
            previous = None
            count = 0
            while count != pos:
                previous = current
                current = current.next_node
                count += 1
            new_node.next_node = current
            previous.next_node = new_node

    def slice(self, start, stop):
        current = self.head
        count = 0
        while count != start:
            current = current.next_node
            count += 1
        result = UnorderedLinkedList()
        result.add(current.data)
        while count < stop-1:
            current = current.next_node
            result.append(current.data)
            count += 1
        return result

    def __repr__(self):
        res = ''
        current = self.head
        while current:
            res += str(current.data) + ' -> '
            current = current.next_node
        return res


my_list = UnorderedLinkedList()

print('Empty: ', my_list.is_empty())

my_list.add(3)
my_list.add(5)
my_list.add(7)
my_list.add(10)
my_list.add(4)
my_list.add(6)
my_list.add(2)

print(my_list)

print('Removing from the middle')
my_list.remove(7)
print(my_list)

print('Removing the head')
my_list.remove(2)
print(my_list)

print('Removing the end')
my_list.remove(3)
print(my_list)

print('Appending to the end')
my_list.append(1)
print(my_list)

print('Index of value 5: ', my_list.index(5))

print('Pop from the end: ', my_list.pop())
print(my_list)

print('Pop by index 0: ', my_list.pop(0))
print(my_list)

my_list.insert(2, 7)
print('Inserting: ', my_list)

print('Slice: ', my_list.slice(1, 3))

print('Size: ', my_list.size())
