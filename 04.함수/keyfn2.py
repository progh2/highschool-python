def fn( a, b, c, d, e ):
  print( a, b, c, d, e)

fn(1, 2, 3, 4, 5)
fn(a=1, b=2, c=3, d=4, e=5)
fn(e=5, d=4, c=3, b=2, a=1)
fn(1, 2, c=3, e=5, d=4)
fn(1, 2, 3, e=5, d=4)
#fn(d=4, e=5, 1, 2, 3)

def fn( a, b, c, *d):
    print(a, b, c, d)

fn( 1, c=3, b=2, 3)