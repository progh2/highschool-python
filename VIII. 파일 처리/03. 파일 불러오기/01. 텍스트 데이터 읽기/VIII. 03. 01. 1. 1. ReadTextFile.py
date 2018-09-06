f = open("text.txt", "w", encoding="utf8")

f.write("안녕하세요.")
f.write("\n")
f.write("반갑습니다.")
f.write("\n")

f.close()

# 파일 읽기

f = open("text.txt", "r", encoding="utf8")

str = f.read()
print(str)

f.close()