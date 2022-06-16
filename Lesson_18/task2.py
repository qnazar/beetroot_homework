import random


class Boss:
    id_s = []  # due to inheritance this attr will be common for both classes and their id will be unique

    @classmethod
    def generate_id(cls):
        """Generation of UNIQUE id"""
        while True:
            id_ = random.randint(1000, 9999)
            if id_ not in cls.id_s:
                cls.id_s.append(id_)
                return id_

    def __init__(self, name: str, company: str):
        self.id = Boss.generate_id()
        self.name = name
        self.company = company
        self.__workers = []

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, new):
        if not isinstance(new, Worker):
            raise TypeError('Only workers can be added')
        # when we try to manually add worker with other Boss to this Boss
        elif new.boss != self:
            raise ValueError('This worker does not work on you')
        else:
            self.__workers.append(new)

    def __str__(self):
        return f'{self.__class__.__name__}: Mr.{self.name} from {self.company}'

    def __repr__(self):
        return f'{self.id}-{self.name}'


class Worker(Boss):
    def __init__(self, name: str, company: str, boss: Boss):
        super().__init__(name, company)
        if isinstance(boss, Boss):
            self.__boss = boss
            self.__boss.workers = self
        else:
            raise TypeError('Boss must be a Boss instance')

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss: Boss):
        if isinstance(boss, Boss):
            self.__boss.workers.remove(self)  # when we are changing workers boss
            self.__boss = boss                # this worker is removed from the list of old boss
            self.__boss.workers.append(self)  # and added to the list of new one
        else:
            raise TypeError('Boss must be a Boss instance')


b1 = Boss('John', 'Henkel')
b2 = Boss('Harry', 'Coca-Cola')

w1 = Worker('Joe', 'Henkel', b1)
w2 = Worker('Zack', 'Coca-Cola', b2)

print(b1.workers)
print(b2.workers)

w2.boss = b1
w1.boss = b2

print(b1.workers)
print(b2.workers)

w2.boss = b2

print(b1.workers)
print(b2.workers)
