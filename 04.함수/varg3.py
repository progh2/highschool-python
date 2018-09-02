def p( space, space_num, *args ):
  str = args[0]
  for i in range(1, len(args)):
    str = str + (space * space_num) + args[i]
  print(str)

p(" ", 2, "♡")
p("/", 1, "♡")
p(",", 3, "♡", "♪")
p("☆", 2, "♡", "♪", "♣")
p("_", 3, "♡", "♪", "♣", "♠")