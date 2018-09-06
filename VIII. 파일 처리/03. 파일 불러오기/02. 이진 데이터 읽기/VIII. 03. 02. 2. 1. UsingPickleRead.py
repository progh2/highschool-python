import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("이름 : " + self.name + "\n나이 : " + str(self.age))

f = open("person_data.bin", "rb")
p = pickle.load(f)
print(p)

f.close()

f = open("persons_data.bin", "rb")
persons = pickle.load(f)

for p in persons:
    print(p)

f.close()