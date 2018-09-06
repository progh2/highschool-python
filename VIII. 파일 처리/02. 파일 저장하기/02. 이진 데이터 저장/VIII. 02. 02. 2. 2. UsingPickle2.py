import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("이름 : " + self.name + "\n나이 : " + str(self.age))

p1 = Person("철수", 20)
p2 = Person("영희", 24)
p3 = Person("주영", 32)

persons = [p1, p2, p3]
f = open("persons_data.bin", "wb")
pickle.dump(persons, f)
f.close()