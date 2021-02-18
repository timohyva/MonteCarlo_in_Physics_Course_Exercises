m=113829760
c=1137
a=3557181

IsRepet=False
RandNum=[]

Ijn1=9
l=0
while IsRepet==False:

      Ij=(a*Ijn1+c)%m
      Ijn1=Ij


      try:
          RandNum.index(Ij)
      except ValueError:
          RandNum.append(Ij)
          l+=1
          print('no repet，the',l,'I is',Ij)
          continue
      else:
          IsRepet=True

print(RandNum)
print('period is',len(RandNum))
