a= int(input("a sayisini giriniz : "))
b= int(input("b sayisini giriniz : "))
c= int(input("c sayisini giriniz : "))

delta = b**2 - 4*a*c
x1= (-b + delta**(1/2))/(2*a)
x2= (-b - delta**(1/2))/(2*a)

if(delta >= 0):
    print("x1 :", x1 , " ; x2 :",x2)
else:
    print("reel kok yoktur")
