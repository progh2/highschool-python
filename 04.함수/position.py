import random

def position(number=20, column=4, title="자리배치"):
    print(title)
    students = list(range(1,number+1))
    random.shuffle(students)
    pos = ""
    for i in range(0, number):
        if students[i] < 10:
          pos =  pos + "0" + str(students[i]) + "번\t"
        else:
          pos =  pos + str(students[i]) + "번\t"
        if  (i + 1) % column == 0: 
            pos =  pos + "\n"  
    print(pos)

position(20, title="3-2반", column=5) 