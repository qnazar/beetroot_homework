import re


class User:
    def __init__(self, email):
        self.email = User.validate(email)

    @classmethod
    def validate(cls, email):
        regex = r'^(?:[a-z0-9]+[._-]?)+[a-z0-9]@[a-z0-9]+[.][a-z]{2,3}$'
        if re.fullmatch(regex, email):
            return email
        raise ValueError('INVALID EMAIL')


u1 = User('qnazar@ukr.net')
u2 = User('something@gmail.com')
u3 = User('many256_andmore58@mail.ua')
