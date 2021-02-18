import random
import math

N=30000 #number of Random numbers
M=62  # how many bins?
Wdt=1/M # width of the bin
E=N/M # expectation values
k=1
chi2=0
y=[]
m=1
NRandNum=[]

##generate random numbers via Random Module, uniform
while m<=N:
      NRandNum.append(random.uniform(0,1))
      m+=1

while k<=M:
      RandNum_k=[n for n in NRandNum if (n > ((k-1)*Wdt))and(n <= (k*Wdt))]
      #print(RandNum_k)
      y.append(len(RandNum_k)) ##save the number in kth bins to faorm a new list
      del RandNum_k
      k+=1

print(y)

for yi in y:
    chi2=chi2+((yi-E)**2)/E
    print(yi,chi2,E)

print('the total number of RN which been classified is', sum(y)) ## show how many rendom numbers are classiied
#print('period is',len(NRandNum))
print('total Chi is',chi2,'\n\n\n')
#print(NRandNum)
