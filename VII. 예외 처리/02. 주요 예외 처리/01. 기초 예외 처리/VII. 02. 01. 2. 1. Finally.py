f = open("file.txt", "w")

try:
    f.write("Hello World")
    f.write(100)
except TypeError:
    print("타입 에러 발생 (100은 쓸 수 없음)")
finally:
    print("에러 여부와 상관 없이 무조건 실행")
    f.close()