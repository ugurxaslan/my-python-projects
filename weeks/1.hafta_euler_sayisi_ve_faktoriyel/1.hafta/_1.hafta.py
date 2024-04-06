def euler():
    n=0
    euler=0
    while(1):
        temp = 1/fak(n)
        if(temp < 0.000000000000001):break
        euler+= temp
        n+=1
    return euler


def fak(a):
    if(a==0 or a==1):
        return 1
    else:
        return a*fak(a-1)


print(euler())