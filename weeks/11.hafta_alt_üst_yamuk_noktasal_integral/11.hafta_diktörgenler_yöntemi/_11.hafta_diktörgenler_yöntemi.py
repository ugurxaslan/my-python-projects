xi=[0,1,2,3,4,5]
yi=[2,3,6,11,18,27]


intgrl_alt,intgrl_ust,intgrl_yamuk=0,0,0
a,b=1,1
n=len(xi)
delta = 2/100

for i in range(n-1):
    intgrl_alt += delta*yi[i]
    intgrl_ust += delta*yi[i+1]
    intgrl_yamuk += delta*(yi[i]+yi[i+1])/2
   

print("alt integral  ",intgrl_alt)
print("ust integral  ",intgrl_ust)
print("yamuk integral  ",intgrl_yamuk)

