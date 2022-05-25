"""You have a list of numbers. Increase each number by 10%.
Use 2 options: lambda function and typical function in Python"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 158, 1.5]
# Option 1
increased = [round(x * 1.1, 2) for x in numbers]
print(increased)

# Option 2
increased = list(map(lambda x: round(x*1.1, 2), numbers))
print(increased)


# Option 3
def increase(nums):
    result = []
    for num in nums:
        result.append(round(num * 1.1, 2))
    return result


print(increase(numbers))
