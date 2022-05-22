# Write a Python program to check whether a given key already exists in a dictionary

city_population = {
    'Kyiv': 2967360,
    'Kharkiv': 1443207,
    'Lviv': 724314,
    'Sniatyn': 9905
}
to_check = input('Enter the key: ')
for key in city_population:
    if key == to_check:
        print(True)
        break
else:
    print(False)
