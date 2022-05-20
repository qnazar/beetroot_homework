"""Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock."""

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# для зручності користуюся списком
result = []
for key in stock.keys():
    result.append(stock[key] * prices[key])
    print('The total price of {}s is {}'.format(key, (stock[key] * prices[key])))

print('The total price of stock is', sum(result))
