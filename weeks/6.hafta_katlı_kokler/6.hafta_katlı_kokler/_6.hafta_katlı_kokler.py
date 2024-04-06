def f(x):
    return x**5-7*x**4+18*x**3-22*x**2+13*x-3
def fx(x):
    return 5*x**4-28*x**3+54*x**2-44*x+13

def per(i,n):
    yuzde = (i / n) * 100
    print(f"%{yuzde:.2f}", end="\r")

x=0
for i in range(12000):
    x = x - f(x)/fx(x)
    per(i,12000)
print("X :",x)