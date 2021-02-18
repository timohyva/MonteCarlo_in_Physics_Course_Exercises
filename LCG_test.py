import os

m=15
c=4
a=7

IsRepet=False
RandNum=[]

Ijn1=4
l=0
while IsRepet==False:

      Ij=(a*Ijn1+c)%m
      Ijn1=Ij


      try:
          RandNum.index(Ij)
      except ValueError:
          RandNum.append(Ij)
          l+=1
          if os.system('reset')==0:
             print('no repet，the',l,'I is',Ij)
             continue

      else:
          IsRepet=True

print(RandNum)
print('period is',len(RandNum))
