class Product:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price


class Article(Product):
    def __init__(self, product: Product, amount):
        self.name = product.name
        self.amount = amount
        self.discount = 0


class Store:
    def __init__(self, id):
        self.id: int = id
        self.profit: 'percent' = 30
        self.goods: dict = {}  # 'name': article
        self.departments: dict = {}  # 'type': [*articles]
        self.income = 0

    def add(self, product: Product, amount: int):
        new = Article(product, amount)
        new.price = round(product.price + product.price * self.profit/100, 2)
        self.goods[new.name] = new
        if product.type not in self.departments.keys():
            self.departments[product.type] = [new]
        else:
            self.departments[product.type].append(new)

    def set_discount(self, identifier, percent, ident_type='name'):
        if percent >= 100:
            raise ValueError('We cannot sell goods for free')
        if ident_type == 'name':
            try:
                self.goods[identifier].discount = percent
            except KeyError:
                raise ValueError('There is no such product in the store')
        elif ident_type == 'type':
            if identifier not in self.departments:
                raise ValueError('There is no such department in the store')
            for article in self.departments[identifier]:
                article.discount = percent
        else:
            raise ValueError('Wrong identifier type')

    def sell(self, product_name, amount):
        try:
            goods = self.goods[product_name]
        except KeyError:
            raise ValueError('There is no such product in the store')
        goods.amount -= amount
        self.income += (goods.price - goods.price * goods.discount/100) * amount

    def get_income(self):
        print(self.income)

    def get_all_products(self):
        for department, goods in self.departments.items():
            print(f'---{department.upper()}---')
            for article in goods:
                print(f'Name: {article.name}')
                print(f'Available: {article.amount}')
                print(f'Price: {article.price}')
                if article.discount:
                    disc_price = round(article.price - article.price * article.discount/100, 2)
                    print(f'DISCOUNT {article.discount}%. Buy now ONLY FOR {disc_price}')
                print()

    def get_product_info(self, product_name):
        print(f'({self.goods[product_name].name}, {self.goods[product_name].amount})')


p1 = Product('Ramen', 'Food', 1.5)
p2 = Product('Apple', 'Food', 1.2)
p3 = Product('Soap', 'Household', 5)
p4 = Product('Fairy', 'Household', 8)
p5 = Product('T-shirt', 'Sport', 30)
p6 = Product('Ball', 'Sport', 20)
prods = {p1: 100, p2: 200, p3: 60, p4: 40, p5: 20, p6: 15}

silpo = Store(123)

for prod, amount in prods.items():
    silpo.add(prod, amount)
silpo.get_all_products()

check = {'Apple': 12, 'Soap': 2, 'T-shirt': 1}
for name, amount in check.items():
    silpo.sell(name, amount)
silpo.get_income()

silpo.set_discount('Household', 15, 'type')
silpo.set_discount('Ball', 25)
silpo.get_all_products()
