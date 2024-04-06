#matrisin köşegen elemanları 0 olmamalı ve görece alt ve üstlerinde büyük olmalıdır
matris = [[7,-1,1,4],
          [1,-6,1,2],
          [1,-1,2,3],
          [2,-4,2,-5]]

vektor=   [11,-2,5,-5]

xi=       [0,1,1,9]

for i in range(2000):
    for j in range(len(xi)):
        temp=0
        for k in range(len(xi)):
            if(k==j):continue
            temp += xi[k]*matris[j][k]

        xi[j] = (vektor[j]-temp)/matris[j][j]
        print(xi)