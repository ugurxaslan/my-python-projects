# 9*x + 3*y + z = 13
#-6*x + 8*z = 2
# 2*x + 5*y - z = 6   

x,y,z = 0,0,0

for i in range(50):
    x=(13-z-3*y)/9
    y=(6-2*x+z)/5
    z=(2+6*x)/8
    print(x,y,z)
