# Write a Python program to convert temperatures to and from celsius, Fahrenheit.
# Formula : c/5 = (f-32)/9 [ where c = temperature in celsius and f = temperature in Fahrenheit.
# Expected Output
# (pay attention to output, students have to practice in string formatting for constructing result message):
#      60°C is 140 in Fahrenheit
#      45°F is 7 in Celsius.
# Use different string formatting!

celsius = int(input('Enter the temperature in Celsius: '))
fahrenheit = celsius * 9/5 + 32
print(f'{celsius}°C is {int(fahrenheit)} in Fahrenheit')

print()

fahrenheit = int(input('Enter the temperature in Fahrenheit: '))
celsius = (fahrenheit - 32) * 5/9
print('{}°F is {} in Celsius'.format(fahrenheit, int(celsius)))
