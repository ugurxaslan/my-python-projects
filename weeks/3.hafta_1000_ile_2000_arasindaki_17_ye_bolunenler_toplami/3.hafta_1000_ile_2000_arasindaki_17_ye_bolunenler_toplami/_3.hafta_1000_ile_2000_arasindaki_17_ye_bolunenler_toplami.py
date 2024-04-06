a=1000
ilk_sayi=1000
toplam=0
for i in range(1000,1017):
    if(i%17==0):
        ilk_sayi=i  
        break

for i in range(ilk_sayi,2000,17):
    toplam+=i

print("toplam :",toplam)