# 기본적인 for 문
for x in range(3, 9, 2):
    print(x)

for ch in "LOVE":
    print(ch)

for item in ["힙합", "발라드"]:
    print(item + " 즐겨듣는다.")

for item in (2560, 1440):
    print(item)

pl = {"C": 1972, "Java": 1995, "Python": 1991}
for key in pl:
    print(key, ":", pl[key])

for item in {"HTML5", "CSS3", "JavaScript"}:
    print(item + "를 할 수 있다.")

# 중첩 반복문
for i in range(1, 9+1):
    print("2 x {} = {}".format(i, 2*i))

for i in range(1, 9+1):
    print("2 x {} = {}".format(i, 2*i))
for i in range(1, 9+1):
    print("3 x {} = {}".format(i, 3*i))
for i in range(1, 9+1):
    print("4 x {} = {}".format(i, 4*i))
for i in range(1, 9+1):
    print("5 x {} = {}".format(i, 5*i))

# 구구단 2~5단을 출력한다.
for dan in range(2, 5+1):
    for i in range(1, 9+1):
        print("{} x {} = {}".format(dan, i, dan*i))

# 리스트 안의 리스트 요소를 출력한다.
table = [["월", "화", "수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col)+" ")
    print()

for i in range(1, 9+1):
    if i == 7:
        break
    print("2 x {} = {}".format(i, 2*i))

for i in range(1, 9+1):
    if i % 2 == 0:
        continue
    print("2 x {} = {}".format(i, 2*i))
