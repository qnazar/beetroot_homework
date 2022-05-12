# Finding the average of 5 numbers using while loop

numbers = [1, 5, 8, 10, -8]
i = 0
suma = 0
while i < len(numbers):
    suma += numbers[i]
    i += 1
average = suma / len(numbers)
print(average)

average = sum(numbers) / len(numbers)
