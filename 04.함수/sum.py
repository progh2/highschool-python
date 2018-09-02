def sum(*numbers):
  sum_value = 0
  for number in numbers:
    sum_value = sum_value + number
  return sum_value

print("1 + 3 = " + str(sum(1,3))) 
print("1 + 3 + 5 + 7 = " + str(sum(1,3,5,7)))
print("1 + 2 + ... + 9 + 10 = " + str(sum(1,2,3,4,5,6,7,8,9,10)))
print("1 + 3 + ... + 100 = " + str(sum( *range(1,100)) ))
