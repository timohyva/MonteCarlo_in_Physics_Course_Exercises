from ctypes import *

xxx=cdll.LoadLibrary("./mt19937-64_5.so")
#a=xxx.main
#a.restype=c_double
#print(xxx.main(),end="")
#a=MAIN()
xxx.main.restype=c_double
num=xxx.main(12345)
print('now it is',num)
