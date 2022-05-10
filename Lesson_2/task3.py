# Create a string s1, calculate the sum and average of the digits that appear in this string,
# ignoring all other characters.

s1 = '123 is not a 456'
count = 0
summary = 0
for char in s1:
    if char.isdigit():
        count += 1
        summary += int(char)
print(f'The SUM is {summary}')
print(f'The AVERAGE is {summary / count}')

print()

s1 = '123 is not a 456'
control_list = []
for char in s1:
    if char.isdigit():
        control_list.append(int(char))
print(f'The SUM is {sum(control_list)}')
print(f'The AVERAGE is {sum(control_list) / len(control_list)}')


