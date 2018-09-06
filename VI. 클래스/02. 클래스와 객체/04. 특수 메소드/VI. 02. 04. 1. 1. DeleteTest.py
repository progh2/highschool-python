class DeletableClass:
    def __del__(self):
        print("delete")

d = DeletableClass()
del d