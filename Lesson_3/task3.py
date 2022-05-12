# Write a python program to find the
# sum of all even numbers from 0 to 10
summary = 0
i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        summary += i
print(summary)
