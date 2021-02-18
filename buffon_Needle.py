import random
import math

L=2
t=10

a=0
b=t/2

c=0
d=(math.pi)/2

N=0
h=0
while N<1000000:
      x=random.uniform(a,b)
      theta=random.uniform(c,d)

      N=N+1

      if x<(L/2)*(math.sin(theta)):
         h=h+1

P=h/N

PI_B=(2*L)/(t*P)
print('Pi may be:',PI_B,'with',N,'times experimrnts')
