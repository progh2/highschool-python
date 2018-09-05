def multi_num(multi, start, end):
  result = []
  for n in range(start, end):
    if n % multi == 0:
      result.append(n)
  return result

multi2 = multi_num(17,1,200)
print("multi_num(17,1,200) : " + str(multi2))
print()
multi3 = multi_num(3,1,100)
print("multi_num(3,1,100) : " + str(multi3))