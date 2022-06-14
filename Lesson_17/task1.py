class Animal:
    def talk(self):
        raise NotImplementedError


class Dog(Animal):
    def talk(self):
        print('Woof woof')


class Cat(Animal):
    def talk(self):
        print('Meow')


def animal_talk(animal):
    animal.talk()


dog = Dog()
cat = Cat()

animal_talk(dog)
animal_talk(cat)
