# 딕셔너리 생성
d = {}; print(d)
urls = {"google": "google.com", 18: "eighteen.gov"};  print(urls)
# 딕셔너리에 요소 추가
urls["x"] = 2560
print(urls)
# 딕셔너리에 요소 수정
urls["x"] = 1920
print(urls)
# 딕셔너리에 요소 제거
del urls["x"];  print(urls)
urls.pop(18);  print(urls)
urls.clear();  print(urls)
# 딕셔너리에서 요소 검색
urls = {"google": "google.com", 18: "eighteen.gov"};  print(urls)
urls.get("google"); print(urls)
print("google" in urls)
print("google.com" in urls)
print("google.com" in urls.values())
# 기타 딕셔너리 관련 함수
print(len(urls))
print(urls.keys())
print(urls.values())
print(urls.items())
