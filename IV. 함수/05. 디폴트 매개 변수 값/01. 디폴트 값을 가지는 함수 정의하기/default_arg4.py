def fn(a, b=[]):
    b.append(a)
    print(b)

fn(3)
fn(5)
fn(10)