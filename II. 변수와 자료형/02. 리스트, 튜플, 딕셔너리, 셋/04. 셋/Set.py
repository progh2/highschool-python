# 셋 생성
game = {"LOL", "Overwatch", "Tetris", 1942, 2048};  print(game)
print(set("Funny"))
print(set([2048, "Tetris", "Cube"]))
print(set((2560, 1440)))
print(set({"google": "google.com", 18: "eighteen.gov"}))
print(set(range(3)))
# 셋에 추가
game.add("Fifa");   print(game)
game.update("NBA", "MLB");   print(game)
# 셋에서 제거
game.remove("LOL"); print(game)
# 셋 연산
s3 = {3, 6, 9, 12}; print(s3)
s4 = {4, 8, 12, 16};    print(s4)
print(s3 & s4)
print(s3.intersection(s4))
print(s3 | s4)
print(s3.union(s4))
print(s3 - s4)
print(s3.difference(s4))
print(s3 ^ s4)
print(s3.symmetric_difference(s4))
