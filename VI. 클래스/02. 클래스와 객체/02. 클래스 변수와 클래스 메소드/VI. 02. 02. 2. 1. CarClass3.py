class Car:
    count = 0

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

print(Car.get_count())
c1 = Car("스포츠카", 100)
c2 = Car("트럭", 50)
print(Car.get_count())
