import sys

def tri_area(width, height):
  return width * height * 1/2

def box_area(width, height):
  return width * height

def print_area(width, height):
  print("가로", width," 세로", height,"인 삼각형의 넓이 :", tri_area(width, height) )
  print("가로", width," 세로", height,"인 사각형의 넓이 :", box_area(width, height) )

if __name__ =="__main__":
  if len(sys.argv) == 3:
    print_area(int(sys.argv[1]), int(sys.argv[2]))
  else:
    print("사용법: python area3 가로 세로")