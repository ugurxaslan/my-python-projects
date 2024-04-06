from math import e

def per(i,n):
    yuzde = (i / n) * 100
    print(f"%{yuzde:.2f}", end="\r")

#f(x)=x**2
#g(x)=3*x+4
#h(x)=f(x)-g(x)
x1,x2=0,0
n=100000
for i in range(n):
    x1 = (3*x1+4)**(1/2)
    x2 = (x2**2-4)/3
    per(i,n)
print("x1 :",x1," | x2 :",x2)
    