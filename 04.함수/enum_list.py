list = [ 'd', 'c', 'a','b']
print("리스트 항목의 수는 ", len(list))
list.reverse()
print("리스트 항목 순서 뒤집기", list )
list.sort()
print("리스트 항목 정렬하기", list)
list.sort(reverse=True)
print("리스트 항목 역정렬하기", list)

for index, value in enumerate(list):
    print("인덱스", index, "위치의 값은 ", value)