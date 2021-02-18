from ctypes import *
import math
import matplotlib.pyplot as plt

#import C library for one time Monte Carlo Simulation
MC_Sim_MBDistri_1Time=cdll.LoadLibrary("./PD_WM_1time.so")
MC_Sim_MBDistri_1Time.main.argtypes=[c_ulonglong,c_ulonglong,c_double]
MC_Sim_MBDistri_1Time.main.restype=c_double

#import C library for refresh seed in everytime running
ReSeed=cdll.LoadLibrary("./Ref_Seed.so")
ReSeed.main.argtypes=[c_ulonglong]
ReSeed.main.restype=c_ulonglong

S0=int(142857197) # primiry seed
N_points=int(1e2) # counts number in one time running
N_run=1000 # How many time to measure
Delta_k=0.001 # Delta_{k} for one time poisson test

l=0
k_Mean_list=[]

while l<N_run:
      print(l,end='  ')
      S1=ReSeed.main(S0)
      S2=ReSeed.main(S1)
      S3=ReSeed.main(S2)
      S0=S3

      # appends the k_{expection} to the list
      k_Mean_list.append(MC_Sim_MBDistri_1Time.main(S3,N_points,Delta_k))
      l=l+1

## the following is for statistical Uncertainty calculation
t=0
k_Start=2.0
k_end=4.0
N_bins=400 # number of bins
Delta_k_WM=(k_end-k_Start)/N_bins
h=[] # un-normlized distribution list of one k
h_normed=[] ## normlized distribution list of one k
H_k=[] # CDF of h
Kh_List=[] #list of k

for i in range(N_bins): # initialized h Kh_List CDF H_k
    #print(i)
    h.append(0.0)
    Kh_List.append(k_Start+(i*Delta_k_WM))
    H_k.append(0.0)

while t<N_run: # take accounts
      e=int((k_Mean_list[t]-k_Start)/Delta_k_WM)
      h[e]+=1
      t+=1

for i in h: #normlize h
    h_normed.append(i/N_run)

for i in range(1,401): # calculate the CDF
    for j in range(i):
        H_k[i-1]+=h_normed[j]

# stardard error via evaluated via Gaussian type
SUM_k=0
for i in k_Mean_list:
    SUM_k+=i

SUM_k2=0
for i in k_Mean_list:
    SUM_k2+=(i-(SUM_k/N_run))**2

sigma=math.sqrt(SUM_k2/N_run)
sigma_k_bar=sigma/math.sqrt(N_run)
print('\n sigma_bar in Gaussian is',sigma_k_bar)

# Plot h_normed
plt.figure()
plt.plot(Kh_List,h_normed,label='1000 runs')
plt.scatter(Kh_List,h_normed,c='r',marker='o',label='1000 runs')
plt.xlim(2.0, 4.0)
plt.ylim(-0.003,0.02)
plt.xlabel("k")
plt.ylabel("Didtribution h of k_bar")
plt.legend(loc='upper left')
plt.show()

# Plot CDF H_K
plt.figure()
plt.plot(Kh_List,H_k,label='1000 runs')
plt.scatter(Kh_List,H_k,c='r',marker='o',label='1000 runs')
plt.xlim(2.0, 4.0)
plt.ylim(-0.05,1.05)
plt.xlabel("k")
plt.ylabel("CDF H_K")
plt.legend(loc='upper left')
plt.show()
