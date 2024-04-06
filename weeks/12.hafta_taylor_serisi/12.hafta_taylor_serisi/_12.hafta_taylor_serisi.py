def f(x):
    return x*(x-1)*(x-1)
 
n=2
h=0.00000001

f1g = (f(n) - f(n-h)) / h
f2g = (f(n) - 2*f(n-h) + f(n-2*h)) / h**2
f3g = (f(n) - 3*f(n-h) + 3*f(n-2*h) - f(n-3*h)) / (h**3)

taylor_fnh = f(n) + h*f1g/1 + h**2*f2g/2 + h**3*f3g/6
print(taylor_fnh)
print(f(n+h))
