def f(x):
    return x**2-3*x-4
# denklemin 2 kökü olmalý

def per(i,n):
    
    yuzde = (i / n) * 100
    print(f"%{yuzde:.2f}", end = "\r")

x1,x2,= -909,909
n=100000
while(1):
    if(f(x1)==0):
         print("kok :",x1)
         break
    if(f(x2)==0):
        print("kok :",x2)
        break
    if(f(x1)*f(x2)<0):
        #kokleri bulma
        for i in range(n):
            xr = (f(x1)*x2-f(x2)*x1)/(f(x1)-f(x2))
            per(i,n)
            if(f(xr)==0):
                print("kok :",xr)
                break
            elif(f(x1)*f(xr)<0):
                x2=xr
            else:
                x1=xr
        break
    #tahminleri duzeltme birini negatif birini pozitif yapma tahminler -1000,1000 olabilir ve bu aralýkta kok vardýr f(x1)*f(x2)>0 olur
    xr = (x1+x2)/2
    if(abs(f(x1))<abs(f(x2))):
        x2=xr
    else:
        x1=xr
    if(x1==x2 and x1*x2!=0):
        print("aralikta kok yok :")
        break

print("x1 :" , x1, "  xr :",xr,"  x2 :",x2)

