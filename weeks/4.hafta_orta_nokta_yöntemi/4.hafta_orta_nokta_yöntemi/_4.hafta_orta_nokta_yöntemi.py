def f(x):
    return x**2-3*x-4
# denklemin 2 kökü olmalý


x1=int(input("x1 :"))
x2=int(input("x2 :"))

while(1):
    if(f(x1)==0):
         print("kok :",x1)
         break
    elif(f(x2)==0):
        print("kok :",x2)
        break
    if(f(x1)*f(x2)<0):
        #kokleri bulma
        while(1):
            xr = (x1+x2)/2
            if(f(xr)==0):
                print("kok :",xr)
                break
            elif(f(x1)*f(xr)<0):
                x2=xr
            else:
                x1=xr
        break
    #tahminleri duzeltme birini negatif birini pozitif yapma tahminlern -1000,1000 olabilir ve bu aralýkta kok vardýr f(x1)*f(x2)>0 olur
    xr = (x1+x2)/2
    if(abs(f(x1))<abs(f(x2))):
        x2=xr
    else:
        x1=xr
    if(x1==x2 and x1*x2!=0):
        print("aralikta kok yok :")
        break


