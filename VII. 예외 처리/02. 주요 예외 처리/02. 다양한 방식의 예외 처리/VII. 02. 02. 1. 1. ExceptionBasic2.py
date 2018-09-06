arr = [1, 2, 3]
try:
    print(arr[4])
except IndexError as e:
    print(e)