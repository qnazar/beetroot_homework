def count_lines(name):
    with open(name, 'r') as file:
        return len(file.readlines())


def count_chars(name):
    with open(name, 'r') as file:
        return len(file.read())


def test(name):
    print('Checking file -', name)
    print('Number of lines is', count_lines(name))
    print('Number of chars is', count_chars(name))
    print('')


if __name__ == '__main__':
    test('text.txt')
    test('mymod.py')
