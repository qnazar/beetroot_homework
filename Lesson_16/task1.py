"""Make a class structure in python representing people at school. Make a base class called Person,
a class called Student, and another one called Teacher. Try to find as many methods and attributes as you can which
belong to different classes, and keep in mind which are common and which are not. For example, the name should be a
Person attribute, while salary should only be available to the teacher. """
from random import choice


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def greeting(self):
        print(f'Hello! My name is {self.name} {self.surname}.')

    def celebrate_birthday(self):
        self.age += 1
        print(f'Happy Birthday! Now you are {self.age}')


class Student(Person):
    def __init__(self, name, surname, age, certificate):
        super().__init__(name, surname, age)
        self.certificate = certificate
        self.tails = []

    def skip_the_lecture(self):
        self.tails.append('lecture')

    def beg_for_exam(self):
        options = (True, False)
        option = choice(options)
        print('You pass the test') if option else print('Retake the test')


class Teacher(Person):
    def __init__(self, name, surname, age, salary, subject):
        super().__init__(name, surname, age)
        self.salary = salary
        self.subject = subject

    def exam_student(self, student):
        if len(student.tails) != 0:
            print('You need to learn harder and clean up your tails.')
            return False
        print('Well done!')
        return True


vika = Teacher('Vika', 'Dvornyk', 24, 3000, 'Python')
nazar = Student('Nazar', 'Klypych', 26, None)

vika.greeting()
nazar.greeting()

nazar.skip_the_lecture()

vika.exam_student(nazar)

nazar.beg_for_exam()

nazar.celebrate_birthday()
vika.celebrate_birthday()
