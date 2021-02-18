#import numpy as np
import matplotlib.pyplot as plt
Nc=[2,3,4]
R_rms=[0.007601924095592709, 0.0023542739713613195,0.0007499459895350159]

plt.semilogx(Nc,R_rms)
plt.scatter(Nc,R_rms,c='r',marker='o',label='log plot of R_rms vs 10^Nc')
plt.xlabel("Nc number of points")
plt.ylabel("R_rms")
plt.legend(loc='upper right')
plt.show()
