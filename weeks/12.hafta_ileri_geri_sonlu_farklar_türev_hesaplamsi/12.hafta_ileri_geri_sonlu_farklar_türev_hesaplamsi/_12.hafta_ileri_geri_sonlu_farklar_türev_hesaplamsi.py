def f(x):
    return x**2+2
 
n=0
h=0.000000001

f1i = (f(n) - f(n+h)) / h
f2i = (f(n) - 2*f(n+h) + f(n+2*h)) / (h**2)
f3i = (f(n) - 3*f(n+h) + 3*f(n+2*h) - f(n+3*h)) / (h**3)

f1g = (f(n) - f(n-h)) / h
f2g = (f(n) - 2*f(n-h) + f(n-2*h)) / h**2
f3g = (f(n) - 3*f(n-h) + 3*f(n-2*h) - f(n-3*h)) / (h**3)

print("ileri fark 1. turev ",f1i)
print("ileri fark 2. turev ",f2i)
print("ileri fark 3. turev ",f3i)
print()
print("geri fark 1. turev ",f1g)
print("geri fark 2. turev ",f2g)
print("geri fark 3. turev ",f3g)