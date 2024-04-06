def f(x,y):
    return x**2+x*y-10
def fx(x,y):
    return 2*x+y
def fy(x,y):
    return x

def g(x,y):
    return y+3*x*y**2-57
def gx(x,y):
    return 3*y**2
def gy(x,y):
    return 1+6*x*y

x=-100000
y=100000
for i in range(100):
    x=x-( (f(x,y)*gy(x,y) - g(x,y)*fy(x,y)) / (fx(x,y)*gy(x,y) - gx(x,y)*fy(x,y)) )

    y=y+( (f(x,y)*gx(x,y) - g(x,y)*fx(x,y)) / (fx(x,y)*gy(x,y) - gx(x,y)*fy(x,y)) )

    print(x,y)