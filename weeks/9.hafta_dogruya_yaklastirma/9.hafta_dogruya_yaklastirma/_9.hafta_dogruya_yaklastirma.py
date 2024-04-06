xi=[1,2,3,4,5,6]
yi=[1,4,9,16,25,36]

n=len(xi)
sum_xiyi,sum_xi2=0,0

for i in range(n):
    sum_xiyi+=xi[i]*yi[i]
    sum_xi2+=xi[i]**2

a1 = (n*sum_xiyi-sum(xi)*sum(yi))/(n*sum_xi2-sum(xi)**2)
a0=(sum(yi)-a1*sum(xi))/n

print("y =",a0,"+",a1,"* x")