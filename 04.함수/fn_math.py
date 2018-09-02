# 절대값
print(10, "의 절대값 : ", abs(10))
print(-10, "의 절대값 : ", abs(-10))
print()
# 10진수 -> 2진수 변환
print(1, "의 2진수 : ", bin(1))
print(3, "의 2진수 : ", bin(3))
print(128, "의 2진수 : ", bin(128))
print(255, "의 2진수 : ", bin(255))
print()
# 10진수 -> 8진수 변환
print(7, "의 8진수 : ", oct(7))
print(8, "의 8진수 : ", oct(8))
print()
# 10진수 -> 16진수 변환
print(9, "의 16진수 : ", hex(9))
print(10, "의 16진수 : ", hex(10))
print(15, "의 16진수 : ", hex(15))
print(16, "의 16진수 : ", hex(16))
print(255, "의 16진수 : ", hex(255))
print()
# 연산
numbers = [ 1, 5, -2, 0, 6 ]
print(numbers, "중 가장 큰 값은 ", max(numbers))
print(numbers, "중 가장 큰 값은 ", min(numbers))
print(numbers, "합계는 ", sum(numbers))
print()
print("2의 10승은", pow(2,10))
print()
pi = 3.14152
print(pi,"의 소숫점 1자리 반올림은", round(pi))
print(pi,"의 소숫점 1자리 반올림은", round(pi,0))
print(pi,"의 소숫점 2자리 반올림은", round(pi,1))
print(pi,"의 소숫점 3자리 반올림은", round(pi,2))
print(pi,"의 소숫점 4자리 반올림은", round(pi,3))