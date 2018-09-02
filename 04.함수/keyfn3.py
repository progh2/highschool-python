def fn( a, b, c, *d ):
  print( a, b, c, d)

# 아래 코드 다 실행 안되는 코드임!
#fn(c=3, b=2, a=1, 4, 5) 
#fn(1, 2, c=3, 4, 5)
fn(4, 5, a=1, b=2, c=3)