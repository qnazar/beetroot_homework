# Create a program that reads the length and width of a farmer’s field from the user.
# Display the area of the field. Hint: The area is 43,5 square km. Use different string formatting!

print('Hello, my dear farmer. Let\'s check your field area.')
length = float(input('Enter the length: '))
width = float(input('Enter the width: '))
area = length * width
print('The area of your field is %.1f square km' % area)
