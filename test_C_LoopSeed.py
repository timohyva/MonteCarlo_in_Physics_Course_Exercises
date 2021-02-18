from ctypes import *

#import random
xxx=cdll.LoadLibrary("./mt19937-64_5.so")
yyy=cdll.LoadLibrary("./mt19937-64_5longlong.so")
#a=xxx.main
#a.restype=c_double
#print(xxx.main(),end="")
#a=MAIN()
xxx.main.argtypes=[c_ulonglong]
xxx.main.restype=c_double

yyy.main.argtypes=[c_ulonglong]
yyy.main.restype=c_ulonglong

S=3243454
l=0
while l<100:

      S=yyy.main(S)
      num=xxx.main(S)
      l+=1
      print(l,'now it is',num,'with S:',S)
      #print(l,'now it is',random.uniform(0,1))
