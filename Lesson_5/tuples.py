# creating tuples
t1 = (1, 2, 3)
t2 = tuple([1, 2, 3])
t3 = (1, )
t4 = tuple()
t5 = ()

# Accessing elements from a Tuple
t = (1, 2, 3, 4, 'five')
print(t[0])

# Add or change items
print(id(t))
t += (8, 7)
print(t)
print(id(t))

# Delete Tuple
tpl = (1, 2, 3, 4, 5)
del tpl
print(tpl)

# Useful methods
print(t.count(1))
print(1 in t)
print(t.index(3))
tpl1 = (1, 2, 3, 4)
tpl2 = (1, 2, 3, 4)
print(tpl1 == tpl2)
print(tpl1 is tpl2)
print(id(tpl1))
print(id(tpl2))
print(tuple(sorted(tpl2)))

# Slicing
a = t[0:-1]
print(a)
b = t[-4:-2:-1]
print(b)
c = t[0:4:2]
print(c)
d = t[::2]
print(d)

# Copy tuple
t_copy = t[:]
print(id(t))
print(id(t_copy))
t_copy = t
print(t_copy)
t += (8, 10)
print(t)
print(t_copy)

# Why tuples are better than lists?
# Memory and speed

# Find maximum from tuple of ints
m = max(t)
print(m)
print(min(t))
print(len(t))





# reverse
seq = (1, 2, 3, 4, 5, 6, 7)
new_seq = list(seq)
new_seq.reverse()
new_seq = tuple(new_seq)
print(new_seq)

# average
average = sum(seq) / len(seq)
print(average)


# compare the size
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# compare the execution time of a list vs. tuple creation statement
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))


