N=10 #number of Random numbers
M=10  # how many bins?
Wdt=1/M # width of the bin
E=N/M # expectation values
k=1
chi2=0
y=[]

NRandNum=[0.12, 0.33, 0.32, 0.78, 0.001, 0.98, 0.56, 0.72, 0.1, 0.2]

while k<=M:
      RandNum_k=[n for n in NRandNum if (n > ((k-1)*Wdt))and(n <= (k*Wdt))]
      print(RandNum_k)
      y.append(len(RandNum_k))
      del RandNum_k
      k+=1

print(y)

for yi in y:
    print(yi)
    chi2=chi2+((yi-E)**2)/E
