class NotEvenNumberError(Exception):
    pass

def even_number_add(a, b):
    if a % 2 != 0 or b % 2 != 0:
        raise NotEvenNumberError
    return a + b

try:
    a = even_number_add(2, 2)
    print("결과값 : " + str(a))
    b = even_number_add(4, 2)
    print("결과값 : " + str(b))
    c = even_number_add(2, 1)
except NotEvenNumberError as e:
    print("짝수만 더할 수 있습니다.")