"""Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax."""


class MyIter:
    """This class makes iterable from int numbers"""
    def __init__(self, num: int):
        self.num = num
        self.seq = MyIter.num_to_seq(num)
        self.index = 0

    def __repr__(self):
        return ''.join([str(n) for n in self.seq])

    @classmethod
    def num_to_seq(cls, num: int) -> list:
        seq = []
        while num != 0:
            seq.append(num % 10)
            num //= 10
        seq.reverse()
        return seq

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.seq[self.index]
        except IndexError:
            raise StopIteration
        finally:
            self.index += 1

    def __getitem__(self, item):
        return self.seq[item]

    def __setitem__(self, key, value):
        self.seq[key] = value


i = MyIter(102436)

print('My view - ', i)

print('Iteration in for loop:')
for item in i:
    print(item, end='   ')
print()

print('Getting item - ', i[4])

i[0] = 8
print('Setting item - ', i)


