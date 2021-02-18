import random

m=113829760
c=1137
a=3557181

IsRepet=False
RandNum=[]
NRandNum=[]

Ijn1=random.uniform(0,100000) ##us random to generate seed
l=1

N=50000 #number of Random numbers
M=62  # how many bins?
Wdt=1/M # width of the bin
E=N/M # expectation values
k=1
chi2=0
y=[]

##generate random numbers via LCG
while IsRepet==False:
      if l>N:
         break

      Ij=(a*Ijn1+c)%m
      Ijn1=Ij

      try:
          RandNum.index(Ij) ## check the repet of random number
      except ValueError:
          RandNum.append(Ij)
          l+=1
          continue
      else:
          IsRepet=True
          print('Repet!!!') ## waring if arrive a period

MaxN=max(RandNum)

##normalization to (0,1)
for rn in RandNum:
    NRandNum.append(rn/MaxN)

while k<=M:
      RandNum_k=[n for n in NRandNum if (n > ((k-1)*Wdt))and(n <= (k*Wdt))]
      y.append(len(RandNum_k)) #save the number in kth bins to form a new lis
      del RandNum_k
      k+=1

print('thet result of classification by bins is',y)

##Chi Square test statistic
for yi in y:
    chi2=chi2+((yi-E)**2)/E
    #print('the yi, chi2 for yi and expectation value are',yi,chi2,E)


print('the total number of RN which been classified is', sum(y)) ## show how many rendom numbers are classiied
#print('period is',len(NRandNum))
print('chi2 is',chi2,'\n\n\n') ##show chi2 square test statistic
#print(NRandNum)
