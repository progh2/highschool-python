import random

# 처음 시작 
n = random.randint(1,6)
print("결과 : " , n)
n = random.randint(1,6)
print("결과 : " , n)
# 다른코드들1.. 
n = random.randint(1,6)
print("결과 : " , n)
# 다른코드들2.. 
n = random.randint(1,6)
print("결과 : " , n)

# 코드 수정 
n = random.randint(1,6)
print("6면 주사위 굴린 결과 : " , n)
n = random.randint(1,6)
print("6면 주사위 굴린 결과 : " , n)
# 다른코드들1.. 
n = random.randint(1,6)
print("6면 주사위 굴린 결과 : " , n)
# 다른코드들2.. 
n = random.randint(1,6)
print("6면 주사위 굴린 결과 : " , n)


# 함수 사용  -- 의미 파악이 쉬워지고 수정이 쉽다
def rolling_dice():
  n = random.randint(1,6)
  print("6면 주사위 굴린 결과 : " , n)
  
rolling_dice()
rolling_dice()
# 다른코드들1.. 
rolling_dice()
# 다른코드들2.. 
rolling_dice()


# 인자값 - 주사위 눈 수 조정 
def rolling_dice(pip):
  n = random.randint(1,pip)
  print(pip, "면 주사위 굴린 결과 : " , n)

rolling_dice(6)
rolling_dice(6)
# 다른코드들1.. 
rolling_dice(10)
# 다른코드들2.. 
rolling_dice(20)
# 인자값 - 주사위 눈 수 조정 
def rolling_dice(pip):
  n = random.randint(1,pip)
  print("주사위 굴린 결과 : " , n)
  return n

# 인자값 - 주사위 여러번 굴리게 하자
def rolling_dice(pip, repeat):
  result = []
  for r in range(1,repeat + 1):
    n = random.randint(1,pip)
    print("주사위 굴린 결과",r," : " , n)
    result.append(n)
  return pip, result

rolling_dice(30, 1)
rolling_dice(30, 2)
r = rolling_dice(30, 3)
print(r[0])
print(r[1])
rolling_dice(30, 0)
rolling_dice(30, -3)


# 인자값 - 주사위 여러번 굴리게 하자
def rolling_dices(*pips):
  result = []
  for pip in pips:
    n = random.randint(1,pip)
    print(pip,"면 주사위 굴린 결과"," : " , n)
    result.append(n)
  return pips, result

print(rolling_dices(6, 12, 20, 60))

print(rolling_dice(repeat=8, pip=3))

def rolling_dice(pip=6, repeat=1):
  result = []
  for r in range(1,repeat + 1):
    n = random.randint(1,pip)
    print("주사위 굴린 결과",r," : " , n)
    result.append(n)
  return pip, result

print(rolling_dice())