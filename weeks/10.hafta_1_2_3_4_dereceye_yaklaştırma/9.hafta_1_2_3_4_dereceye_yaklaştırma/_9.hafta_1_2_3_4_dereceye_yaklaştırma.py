import numpy as np

def dort(xi,yi):
    n=len(xi)
    sum_xiyi,sum_xi2yi,sum_xi3yi,sum_xi4yi=0,0,0,0
    sum_xi2,sum_xi3,sum_xi4,sum_xi5,sum_xi6,sum_xi7,sum_xi8=0,0,0,0,0,0,0

    for i in range(n):
        sum_xiyi+=xi[i]*yi[i]
        sum_xi2yi+=xi[i]**2*yi[i]
        sum_xi3yi+=xi[i]**3*yi[i]
        sum_xi4yi+=xi[i]**4*yi[i]

        sum_xi2+=xi[i]**2
        sum_xi3+=xi[i]**3
        sum_xi4+=xi[i]**4
        sum_xi5+=xi[i]**5
        sum_xi6+=xi[i]**6
        sum_xi7+=xi[i]**7
        sum_xi8+=xi[i]**8

    matris=[[n,sum(xi),sum_xi2,sum_xi3,sum_xi4],
            [sum(xi),sum_xi2,sum_xi3,sum_xi4,sum_xi5],
            [sum_xi2,sum_xi3,sum_xi4,sum_xi5,sum_xi6],
            [sum_xi3,sum_xi4,sum_xi5,sum_xi6,sum_xi7],
            [sum_xi4,sum_xi5,sum_xi6,sum_xi7,sum_xi8]]

    vektor=[sum(yi),sum_xiyi,sum_xi2yi,sum_xi3yi,sum_xi4yi]

    xt=[0,1,2,3,5]
    temp1=[0,0,0,0,0]
    for i in range(500000):
        for j in range(len(xt)):
            temp=0
            for k in range(len(xt)):
                if(k==j):continue
                temp += xt[k]*matris[j][k]

            xt[j] = (vektor[j]-temp)/matris[j][j]
            print(xt)

    for i in range(len(xt)):
        if(abs(xt[i])<0.0000001):xt[i]=0

    matris = np.array(matris)
    print(matris)
    vektor=np.array(vektor)
    print(vektor)
    return xt

def uc(xi,yi):
    n=len(xi)
    sum_xiyi,sum_xi2yi,sum_xi3yi=0,0,0
    sum_xi2,sum_xi3,sum_xi4,sum_xi5,sum_xi6=0,0,0,0,0

    for i in range(n):
        sum_xiyi+=xi[i]*yi[i]
        sum_xi2yi+=(xi[i]**2)*yi[i]
        sum_xi3yi+=(xi[i]**3)*yi[i]

        sum_xi2+=xi[i]**2
        sum_xi3+=xi[i]**3
        sum_xi4+=xi[i]**4
        sum_xi5+=xi[i]**5
        sum_xi6+=xi[i]**6

    matris=[[n,sum(xi),sum_xi2,sum_xi3],
            [sum(xi),sum_xi2,sum_xi3,sum_xi4],
            [sum_xi2,sum_xi3,sum_xi4,sum_xi5],
            [sum_xi3,sum_xi4,sum_xi5,sum_xi6]]

    vektor=[sum(yi),sum_xiyi,sum_xi2yi,sum_xi3yi]

    xt=[0,1,1,1]

    for i in range(100000):
        for j in range(len(xt)):
            temp=0
            for k in range(len(xt)):
                if(k==j):continue
                temp += xt[k]*matris[j][k]

            xt[j] = (vektor[j]-temp)/matris[j][j]
            print(xt)

    for i in range(len(xt)):
        if(abs(xt[i])<0.0000001):xt[i]=0

    matris = np.array(matris)
    print(matris)
    vektor=np.array(vektor)
    print(vektor)
    return xt

def iki(xi,yi):
    n=len(xi)
    sum_xiyi,sum_xi2yi=0,0
    sum_xi2,sum_xi3,sum_xi4=0,0,0

    for i in range(n):
        sum_xiyi+=xi[i]*yi[i]
        sum_xi2yi+=xi[i]**2*yi[i]

        sum_xi2+=xi[i]**2
        sum_xi3+=xi[i]**3
        sum_xi4+=xi[i]**4

    matris=[[n,sum(xi),sum_xi2],
            [sum(xi),sum_xi2,sum_xi3],
            [sum_xi2,sum_xi3,sum_xi4]]

    vektor=[sum(yi),sum_xiyi,sum_xi2yi]

    xt=[0,1,2]

    for i in range(10000):
        for j in range(len(xt)):
            temp=0
            for k in range(len(xt)):
                if(k==j):continue
                temp += xt[k]*matris[j][k]

            xt[j] = (vektor[j]-temp)/matris[j][j]
            print(xt)

    for i in range(len(xt)):
        if(abs(xt[i])<0.0000001):xt[i]=0

    matris = np.array(matris)
    print("matris\n",matris)
    vektor=np.array(vektor)
    print("vektor\n",vektor)
    return xt

def bir(xi,yi):
    n=len(xi)
    sum_xiyi=0
    sum_xi2=0

    for i in range(n):
        sum_xiyi+=xi[i]*yi[i]
        sum_xi2+=xi[i]**2

    matris=[[n,sum(xi)],
            [sum(xi),sum_xi2]]

    vektor=[sum(yi),sum_xiyi]

    xt=[0,1]

    for i in range(10000):
        for j in range(len(xt)):
            temp=0
            for k in range(len(xt)):
                if(k==j):continue
                temp += xt[k]*matris[j][k]

            xt[j] = (vektor[j]-temp)/matris[j][j]
            print(xt)

    for i in range(len(xt)):
        if(abs(xt[i])<0.0000001):xt[i]=0

    matris = np.array(matris)
    print(matris)
    vektor=np.array(vektor)
    print(vektor)
    return xt

xi=[0,1,2,3,4,5]
yi=[0,1,4,9,16,25]

#print(bir(xi,yi))
#rint(iki(xi,yi))
print(uc(xi,yi))
#print(dort(xi,yi))
#burdaki amaç bir dizi (x,y) nokltalarý verilir öyle bir denkem seçelim ki her 
#(x,y) ile (x,f(x)) noktalarýnýn uzaklýðý yani |y-f(x)| deðerleri toplamý minimum olsun