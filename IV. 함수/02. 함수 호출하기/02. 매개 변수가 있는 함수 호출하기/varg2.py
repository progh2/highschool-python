def p( *args ):
  str = ""
  for a in args:
    str = str + a
  print(str)

p()
p("♡")
p("♡", "♪")
p("♡", "♪", "♣")
p("♡", "♪", "♣", "♠")