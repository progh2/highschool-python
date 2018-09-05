import random

# 인자값 - 주사위 여러번 굴리게 하자
def rolling_dice(pip, repeat):
  result = []
  for r in range(1,repeat + 1):
    n = random.randint(1,pip)
    print("주사위 굴린 결과",r," : " , n)

rolling_dice(6, 1)
rolling_dice(6, 2)
# 다른코드들1.. 
rolling_dice(10, 0)
# 다른코드들2.. 
rolling_dice(20, -3)
