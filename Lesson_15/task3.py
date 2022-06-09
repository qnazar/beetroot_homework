"""Create a class of triangles, the variables of which are the sides of the triangle, and the methods of calculating its
area and perimeter. Create two objects that belong to the created class, and calculate the area for one
and the perimeter for the other."""


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        """Формула Герона"""
        p = self.get_perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


t1 = Triangle(5, 6, 8)
print(t1.get_perimeter())

t2 = Triangle(3, 4, 5)
print(t2.get_area())
