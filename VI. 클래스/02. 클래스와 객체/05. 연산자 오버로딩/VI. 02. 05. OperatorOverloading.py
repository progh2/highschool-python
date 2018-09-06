class MyNumber:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print("__add__")
        return MyNumber(self.val + other.val)

    def __sub__(self, other):
        print("__sub__")
        return MyNumber(self.val - other.val)

    def __mul__(self, other):
        print("__mul__")
        return MyNumber(self.val * other.val)

    def __truediv__(self, other):
        print("__truediv__")
        return MyNumber(self.val / other.val)

n1 = MyNumber(2)
n2 = MyNumber(3)

n3 = n1 + n2
print(n3.val)

n4 = n1 - n2
print(n4.val)

n5 = n1 * n2
print(n5.val)

n6 = n1 / n2
print(n6.val)

