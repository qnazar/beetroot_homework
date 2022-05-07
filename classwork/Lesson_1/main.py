from math import sin
# task 1
print('Mary had a little lamb,', '\tLittle lamb,little lamb,', '\t\tMary had a little lamb,',
      '\t\tIts fleece was white as snow,', 'And every where that Mary went,', '\tMary went, Mary went', sep='\n')
# task 2
print(11, 12, 2014, sep='/')
print(11, 12, 2014, sep='-')
print(11, 12, 2014, sep=' ')
print(11, 12, 2014, sep='')


# additional tasks

# маючи основу і висоту
def triangle_area_simple(a, h):
    print(a * h * 0.5)


triangle_area_simple(5, 4)


# маючи дві сторони і кут між ними
def triangle_area(a, b, angle):
    print(0.5 * a * b * sin(angle))


triangle_area(10, 4, 90)


# числа, кратні семи
def multiseven_for(value):
    for i in range(1, value+1):
        print(i * 7)


multiseven_for(7)


def multiseven_while(value):
    counter = 1
    while counter <= value:
        print(counter * 7)
        counter += 1


multiseven_while(7)


def median(a, b, c):
    if a > b > c or a < b < c:
        print(b)
    elif b > a > c or b < a < c:
        print(a)
    else:
        print(c)


median(5, 15, -10)


