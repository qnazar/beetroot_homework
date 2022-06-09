"""Create a Parcel class that contains the following attributes: width, length, height. The class also contains a field
to count the number of parcels. Create an array of objects such as "Parcel". You can give this array
Create several objects of the "Parcel" class and write them in an array. Find the smallest parcel. Check the number of
existing parcels. If this value exceeds any limit value - display a message."""


class Parcel:

    count = 0
    limit = 5

    def __init__(self, width, length, height):
        if not Parcel.check_the_limit():
            print('You are out of limit!!!')
            return
        self.width = width
        self.length = length
        self.height = height
        Parcel.count += 1
        Parcel.limit -= 1
        self.volume = self.get_volume()

    def get_volume(self):
        return self.width * self.height * self.length

    @classmethod
    def check_the_limit(cls):
        if Parcel.limit <= 0:
            return False
        return True


p1 = Parcel(2, 3, 4)
p2 = Parcel(1, 5, 2)
p3 = Parcel(2, 2, 2)
p4 = Parcel(2, 2, 2)
p5 = Parcel(2, 2, 2)
# p6 = Parcel(1, 1, 1)


array_of_parcels = [p1, p2, p3]
min_parcel = min([i.volume for i in array_of_parcels])
print(min_parcel)

print(Parcel.count)

# p1.check_the_limit()


