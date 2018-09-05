import random

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
