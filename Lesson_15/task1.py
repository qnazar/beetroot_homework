"""Write a "Student" class that contains information about the name and surname. The class must contain a constructor.
Contains information about ZNO, student's CERTIFICATE (атестат). Create multiple student class objects.
Calculate and display the rating of each student.
"""


class Student:
    def __init__(self, name, surname, zno, certificate):
        self.name = name
        self.surname = surname
        self.zno = zno
        self.certificate = certificate

    def get_rating(self):
        return self.zno + self.certificate


s1 = Student('Nazar', 'Klypych', 580, 198)
s2 = Student('Pavlo', 'Shchur', 582, 197)
s3 = Student('Oleksii', 'Borodin', 590, 190)

print(s1.get_rating())
print(s2.get_rating())
print(s3.get_rating())
