# 리스트 생성
l = []; print(l)
player = ["Messi", 10, True];   print(player)
print(list("Happy"))
print(list((1125, 2436)))
print(list({"menu": "pizza", "price": 10000}))
print(list({"사과", "배"}))
nums = list(range(3));  print(nums)
# 리스트에 요소 추가
print(nums + [10, 11])
nums += [10, 11];   print(nums)
nums.append(20);    print(nums)
nums.append([30, 31]);  print(nums)
nums.insert(2, 40); print(nums)
nums.extend([50, 51]);  print(nums)
# 리스트에 요소 수정
print(nums[7])
nums[7] = 60;   print(nums)
# 리스트에서 요소 제거
del nums[2];    print(nums)
nums.remove(20);    print(nums)
nums.pop();    print(nums)
nums.pop(5);    print(nums)
nums.clear();    print(nums)
# 리스트에서 요소 검색
nums = list(range(3));  print(nums)
nums += [100, 10];  print(nums)
print(nums[3])
print(3 in nums)
print(10 in nums)
# 기타 리스트 관련 함수
print(len(nums))
nums.sort();    print(nums)
nums.reverse();    print(nums)
# range() 함수
print(range(3))
print(range(1, 10))
print(range(1, 10, 2))
print(set(range(1, 10, 2)))
print(list(range(1, -5, -2)))
for i in range(3):
    print(i)
