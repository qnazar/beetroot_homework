"""Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and
the number of occurrences as values. """

string = input('Enter the string: ').casefold().split(sep=' ')
# checking the punctuation to have more valid result
punctuation = ',.:;"-'
for word in string:
    for char in word:
        if char in punctuation:
            string[string.index(word)] = word.replace(char, '')

result = {}
for word in string:
    if word not in result:
        count = string.count(word)
        result[word] = count
print(result)


# or with dict comprehension but without checking the punctuation
result = {word: string.count(word) for word in string if word.isalpha()}
print(result)
