def min_man(*args):
  min = args[0]
  max = args[0]
  for arg in args:
    if min > arg:
      min = arg
    if max < arg:
      max = arg
  return min, max

print(min_man(52, -3, 23, 89, -21))
min_value, max_value = min_man(52, -3, 23, 89, -21)
print("최저값: " + str(min_value))
print("최고값: " + str(max_value))