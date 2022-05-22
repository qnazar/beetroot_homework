# Produce a list containing the word ‘minus’ if a number in the numbers is < 0,
# and the word ‘plus’ if the number is > 0.
# Result would look like [‘plus’, ’plus’, ‘minus’]

numbers = [-1, 5, 7, -7, -8, 10]
result = ['minus' if i < 0 else 'plus' for i in numbers]
print(result)
