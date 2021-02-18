import random
import math
import matplotlib.pyplot as plt

L=2
t=10

a=0
b=t/2

c=0
d=(math.pi)/2

HowManyTimes=[10,100,1000,1e4]
x=list(range(1,len(HowManyTimes)+2))
PI_B_I=[]

for I in range(len(HowManyTimes)):
    print(HowManyTimes[I])

    N=0
    h=0

    Ntimes=0
    htimes=0

    while N<100:

          xlist=[]
          thetalist=[]
          H=0
          M=0
          while M<HowManyTimes[I]:

                xlist.append(random.uniform(a,b))
                thetalist.append(random.uniform(c,d))
                M=M+1

    #  print(xlist)
    #  print(thetalist)

          Ntimes=Ntimes+len(xlist)
          for l in range(len(xlist)):
              if xlist[l]<(L/2)*(math.sin(thetalist[l])):
                 H=H+1
          htimes=htimes+H
          N=N+1

    print(Ntimes,htimes)
    P=htimes/Ntimes

    PI_B=(2*L)/(t*P)
    PI_B_I.append(PI_B)
    print('Pi may be:',PI_B,'with',N*M,'times experimrnts')


PI_B_I.append(math.pi)
plt.scatter(x,PI_B_I)
plt.show()
