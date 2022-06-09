"""Write a class that contains information about the country with the following attributes: name, capital, population,
currency. Create two objects of this class, initialize their fields. Display a country with a larger population.
Create a third object in this class. Change the value of a currency in this object."""


class Country:

    countries = []

    def __init__(self, name, capital, population, currency):
        self.name = name
        self.capital = capital
        self.population = population
        self.currency = currency
        Country.countries.append(self)

    @classmethod
    def get_largest(cls):
        largest = cls.countries[0]
        for country in cls.countries:
            if country.population > largest.population:
                largest = country
        print(f'The largest country is {largest.name} with population {largest.population}!')
        return largest


ua = Country('Ukraine', 'Kyiv', 40000000, 'UAH')
th = Country('Thailand', 'Bangkok', 70000000, 'THB')

Country.get_largest()

sp = Country('Spain', 'Madrid', 47350000, 'PES')
sp.currency = 'EUR'
print(sp.currency)
