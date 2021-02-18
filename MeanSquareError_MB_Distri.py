from ctypes import *
import math

#import C library for one time Monte Carlo Simulation
MC_Sim_MBDistri_1Time=cdll.LoadLibrary("./MC_MB_1Time.so")
MC_Sim_MBDistri_1Time.main.argtypes=[c_ulonglong,c_ulonglong,c_double]
MC_Sim_MBDistri_1Time.main.restype=c_double

#import C library for refresh seed in everytime running
ReSeed=cdll.LoadLibrary("./refresh_seed.so")
ReSeed.main.argtypes=[c_ulonglong]
ReSeed.main.restype=c_ulonglong

kb=8.6173324E-5
T=600.0
E_theorical=(3/2)*(kb*T)

S0=int(142857197) # primiry seed
N_points=int(1e3) # counts number in one time running
N_run=500
Delta_E=0.00001
l=0
Elist=[]
Esum2=0
while l<N_run:
      print(l,end='  ')
      S1=ReSeed.main(S0)
      S2=ReSeed.main(S1)
      S3=ReSeed.main(S2)
      S0=S3

      # appends the E_{expection} to the list
      Elist.append(MC_Sim_MBDistri_1Time.main(S3,N_points,Delta_E))
      # sum (E_l-E_theorical)^2
      Esum2+=(Elist[l]-E_theorical)**2
      l=l+1

R_rms=math.sqrt((1/N_run)*Esum2)
print('\nR_rms=',R_rms,'with Delta_E',Delta_E)
print("\n\n\n",Elist)
