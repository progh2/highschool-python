# 튜플 생성
t = ();  print(t)
xy = (2560, 1440);  print(xy)
color = 129, 247, 216;  print(color)
print(xy + color)
print(xy * 2)
# 패킹과 언패킹
color = 129, 257, 216;  print(color)
red, green, blue = color
print(red)
print(green)
print(blue)
x, y = 1920, 1080;  print(x, y)
print(x)
print(y)
# 튜플 활용
x = 2560
y = 1440
x, y = y, x
print(x)
print(y)
a = (123, "abc", True, 123)
print(a[1])
print(a[2:])
print(a[:2])
# a[1] = 3
print(a.index("abc"))
print(a.count(123))
