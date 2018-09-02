def star(mark, *args):
  for arg in args:
      print(mark * arg)

star("♬", 3)
star("♡", 1, 2, 3)
star("♣", 5, 3, 1)