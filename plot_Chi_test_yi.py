import matplotlib.pyplot as plt

a=[517, 475, 489, 495, 484, 504, 476, 477, 513, 478, 500, 487, 485, 446, 468, 469, 512, 448, 476, 487, 498, 470, 484, 502, 459, 496, 514, 488, 500, 483, 488, 488, 467, 518, 479, 461, 509, 492, 476, 492, 499, 489, 495, 492, 472, 463, 525, 440, 442, 485, 471, 483, 482, 477, 463, 456, 487, 443, 491, 495, 529, 471]
#a=[3085, 3106, 2977, 3004, 2931, 2944, 2952, 3043, 3015, 2943]

E=483
M=62

l=1
x=list(range(E-100,E+100))
distribution=[]

print(len(x))

for X in x:
      print(X)
      d=[n for n in a if n==X]
      print(d)
      distribution.append(len(d))
      #print(distribution)
      l+=1

print(len(distribution))
plt.scatter(x,distribution)
plt.show()
