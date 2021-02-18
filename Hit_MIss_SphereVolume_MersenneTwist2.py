import math
from ctypes import *


def f_xi(point_list):
    x2=0
    for xi in point_list[0:(len(point_list)-1)]:
        x2=xi**2+x2

    if 1-x2>=point_list[-1]**2:
        return 1
    else:
        return 0

N=10e6 # No. of total points
N_total=0 # loop amount
N_hit=0 # hit loop

M=9 #dimension of sphere
Ve=(3**M)*1.5 # volume of external retangle

MersenneTwister=cdll.LoadLibrary("./mt19937-64_5.so")
MersenneTwister.main.argtypes=[c_ulonglong]
MersenneTwister.main.restype=c_double

MTS=cdll.LoadLibrary("./mt19937-64_5_longlong.so")
MTS.main.argtypes=[c_ulonglong]
MTS.main.restype=c_ulonglong

S=6786273

while N_total<=N:

      l=1
      xi=[] # initializes the random vector
      while l<M+1:
            S=MTS.main(S)
            xi.append((MersenneTwister.main(S))*3-1.5) # basic manifold points

            l+=1
      else:
            S=MTS.main(S)
            xi.append(MersenneTwister.main(S)*1.5) # hight point

      if f_xi(xi)==1: # judge in voi out
         N_hit+=1

      N_total+=1

fh=N_hit/N_total
V_sphere=2*(Ve*fh)
sigma_Vbar=Ve*((math.sqrt(N_hit-(N_hit**2/N)))/N_total)

print('the volume of',M,'dimension shpere is:',V_sphere,'with standard error of mean',sigma_Vbar,'via MersenneTwister and',N,'points')
