user_name = input("당신의 이름은? ")
user_age = input("당신의 나이는? ")
print(user_name + "님! 당신의 나이는 " + str(user_age) + "세 이군요!")
say = "{0}님! 당신의 나이는 {1}세 이군요! 나이가 {1}라니 놀라워요!"
print(say.format(user_name, user_age))
print()

pi = "3.14159"
print(float(pi) + 100)
print()
year = "2018"
print("100년 뒤라면 " , int(year) + 100 , "년 입니다.")
print()
print("숫자 등을 문자열로 변환하려면 str()을 이용합니다.")
print("올해는 " + str(year) + "년 입니다")