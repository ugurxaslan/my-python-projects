def dif(x,y):
    return -y/x

def per(i,n):
    
    yuzde = (i / n) * 100
    print(f"%{yuzde:.2f}", end="\r")

h=0.00001
a=4
b=7
y=0.75
n=int((b-a)/h)

for i in range(n):
    y+=dif(a,y)*h
    a+=h
    if(i%100==0):
        per(i,n)
print("    euler metodu ile :",y)

a=4
y=0.75
n=int((b-a)/h)

for i in range(2*n):
    y+=dif(a,y)*h/2
    a+=h/2
    if(i%100==0):
        per(i,2*n)
print("iyi euler metodu ile :",y)

a=4
y=0.75
n=int((b-a)/h)

for i in range(n):
    y0=y+dif(a,y)*h
    y+=(dif(a,y)+dif(a,y0))*h/2
    a+=h
    if(i%100==0):
        per(i,n)
print("     heun metodu ile :",y)
