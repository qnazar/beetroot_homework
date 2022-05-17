# Generate 10 random integers between 1 and 1000 which is divisible by 5
from random import randint
result = []
while len(result) < 10:
    a = randint(1, 1000)
    if a % 5 == 0 and a not in result:
        result.append(a)
print(result)
