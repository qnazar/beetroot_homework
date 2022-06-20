"""Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
`start`, `end`, and optional step. Tips: See the documentation for `range` function"""


def in_range(start, end, step=1):
    while start != end:
        yield start
        start += step


for i in in_range(0, 10):
    print(i, end=' ')

print()

for i in in_range(10, 0, -1):
    print(i, end=' ')

print()

for i in in_range(0, 20, 2):
    print(i, end=' ')
