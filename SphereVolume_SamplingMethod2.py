from ctypes import *

SphereVolume_SM=cdll.LoadLibrary("./SV_SM.so")
SphereVolume_SM.main.argtypes=[c_double,c_double,c_uint]
SphereVolume_SM.main.restype=c_double

N2=6e7
N1=5e6
V_Mn1=1.86582079
Dim_Base=11

Max_Dim=15
N=N1
while Dim_Base<=Max_Dim:
      
      if Dim_Base>=9:
         N=N2

      V_M=SphereVolume_SM.main(N,V_Mn1,Dim_Base)
      Dim_Base=Dim_Base+1
      V_Mn1=V_M
      
