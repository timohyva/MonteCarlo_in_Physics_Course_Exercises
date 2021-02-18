import random
import math
import matplotlib.pyplot as plt

L=2
t=10

a=0
b=t/2

c=0
d=(math.pi)/2

HowManyTimes=[90,900,9000,9*1e4]
x=list(range(1,len(HowManyTimes)+1))
EPI_I=[]

for I in range(len(HowManyTimes)):
    print(HowManyTimes[I])

    N=0
    PI_B=[]
    while N<100:

          xlist=[]
          thetalist=[]
          H=0
          M=0
          while M<HowManyTimes[I]:

                xlist.append(random.uniform(a,b))
                thetalist.append(random.uniform(c,d))
                M=M+1


#          print(xlist)
#          print(thetalist)


          for l in range(len(xlist)):
              if xlist[l]<(L/2)*(math.sin(thetalist[l])):
                 H=H+1

          P=H/M 
          Pi_Nth=(2*L)/(t*P)
          PI_B.append(Pi_Nth)
          N=N+1

    SUM=0
    for ll in range(len(PI_B)):
        SUM=SUM+math.fabs(PI_B[ll]-math.pi) 


    EPI_I.append(SUM/N)


plt.scatter(x,EPI_I)
plt.show()
