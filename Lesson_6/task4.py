# Write a program to sum all the values in a dictionary

city_population = {
    'Kyiv': 2967360,
    'Kharkiv': 1443207,
    'Lviv': 724314,
    'Sniatyn': 9905}

result = sum([i for i in city_population.values()])
print(result)
