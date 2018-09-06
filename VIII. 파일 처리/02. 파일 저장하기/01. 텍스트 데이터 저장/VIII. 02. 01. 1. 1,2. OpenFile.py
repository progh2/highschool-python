f = open("file.txt", "w")

f.write("hello")
f.write("\n")
f.write("world")

f = open("file.txt", "a")

f.write("\n")
f.write("append")
