import matplotlib.pyplot as plt
import numpy as np

R_rms= [0.0034168087771400085, 0.0027815582326081697, 0.0024022247071169684, 0.0023773820903603515, 0.002365677458581484, 0.0023580336577812733, 0.0023542739713613195, 0.002354001165393945, 0.0023539625330320996, 0.002353948208560094, 0.002353968337383678] 


Delta_E=[0.005, 0.003, 0.001, 0.0007, 0.0005, 0.0003, 0.0001, 7e-05, 5e-05, 3e-05, 1e-05]

plt.figure()  
plt.plot(Delta_E,R_rms,label='N_{c}=1000 points test')  
plt.scatter(Delta_E,R_rms,c='r',marker='o',label='N_{c}=1000 points test')
plt.xlim(-0.00005, 0.0051)
plt.ylim(0.002253968337383678,0.0035168087771400085)
plt.xlabel("\Delta_E")
plt.ylabel("R_{rms}")
plt.legend(loc='upper left')
plt.show()
