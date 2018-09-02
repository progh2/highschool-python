# star함수 정의
def star(mark, repeat, space, space_repeat, line):
  for i in range(0, line):
    str = mark
    for j in range(1, repeat):
      str = str + (space * space_repeat) + mark
    print(str) 


star( "※※※", 3, "_", 2, 5)