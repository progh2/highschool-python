import hello_func
import greeting_func

def main():
  print("insa모듈입니다.")
  print("__name__ : ", __name__)  # 실행하면 main이 출력된다.
  hello_func.hello()
  greeting_func.greeting()

main()
