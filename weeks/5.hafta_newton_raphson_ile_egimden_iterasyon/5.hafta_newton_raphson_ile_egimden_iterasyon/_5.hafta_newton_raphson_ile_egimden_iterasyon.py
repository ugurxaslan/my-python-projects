def f(x):
    return x**2-3*x-4 
def ft(x):
    return 2*x-3

x=-5152
for i in range(100):
    x = x - (f(x)/ft(x))
    print(i,"-",x)