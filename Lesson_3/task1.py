# Write a Python program to check whether an alphabet is a vowel or
# consonant.

letter = ''
vowels = 'aeiou'
if letter.casefold() in vowels.casefold():
    print('It is a vowel!')
else:
    print('It is a consonant')

