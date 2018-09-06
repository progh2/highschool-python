f = open("text.txt", "r", encoding="utf8")

line1 = f.readline()
print("line 1 : " + line1)
line2 = f.readline()
print("line 2 : " + line2)
line3 = f.readline()
print("line 3 : " + line3)

f.close()