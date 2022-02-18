def simplegeneratorfun(a,b):
    yield a+b
    yield a-b
for i in simplegeneratorfun(4,7):
    print(i)