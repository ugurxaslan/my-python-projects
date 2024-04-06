def f(x):
    return x**2-2*x-8

x1=10
x2=100

while(f(x1)!=f(x2)):
    x3 = x2 - ( ( f(x2)*(x1-x2) ) / ( f(x1)-f(x2) ) )
    x1=x2
    x2=x3
    print(x2)