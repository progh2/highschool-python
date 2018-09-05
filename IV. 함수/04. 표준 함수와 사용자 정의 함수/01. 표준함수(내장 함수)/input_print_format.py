user_name = input("이름은? ")
user_age = input("나이는? ")
print(user_name + "님! 나이는 " + str(user_age) + "세군요!")
say = "{0}님! 나이는 {1}세군요! {1}세라니 놀라워요!"
print(say.format(user_name, user_age))
