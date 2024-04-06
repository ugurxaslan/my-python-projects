def f(x):
    return 1/x
#önce geçmiþ fonksiyonlarýmýz ile noktalarýmýzý bir fonsiyna yaklaþtýrýp sonra integral alýyoruz


integral=0
a,b=0,1
#a,b=-1,0
n = 1000000
delta = (b-a)/n

for i in range(n-1):
    integral += delta*(f(a+delta) + f(a+2*delta))/2
    a+=delta
    yuzde = (i / n) * 100

    
    print(f"%{yuzde:.2f} :",integral, end="\r")

print("integral :",integral)
