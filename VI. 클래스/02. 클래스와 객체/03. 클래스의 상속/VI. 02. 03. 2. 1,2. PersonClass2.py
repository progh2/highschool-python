class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name + "가 " + food + "를 먹습니다.")

    def __str__(self):
        return self.name + " : " + str(self.age)


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def work(self):
        print("열심히 일을 합니다.")

    def get_salary(self):
        print("급료를 받습니다.")
        return self.salary

e = Employee("영희", 19, 100)
e.eat("밥")
e.work()
print(e)
r = e.get_salary()
print(r)

