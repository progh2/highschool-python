import sys

def repeat_str(msg, n):
    # 코드 작성

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(repeat_str(sys.argv[1], int(sys.argv[2])))
    else:
        print("사용법 : python repeat_str 문자열 숫자")