import sys as s

sys = "반복 시스템입니다."

while True:
  print(sys)
  print( "종료하려면 exit를 입력하세요" )
  user_input = input("> ")
  if user_input == "exit":
    s.exit()