import random

def dice(pip):
  result = random.randint(1,pip)
  # 여기에 코드 추가
  return result

print("6면의 주사위의 값은 : " + str(dice(6)))
