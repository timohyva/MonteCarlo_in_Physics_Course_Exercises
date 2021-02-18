import matplotlib.pyplot as plt

a=[807, 807, 802, 812, 800, 817, 802, 807, 796, 820, 797, 809, 804, 804, 803, 810, 807, 807, 811, 799, 807, 807, 818, 799, 801, 804, 816, 807, 805, 806, 804, 809, 807, 808, 808, 809, 798, 807, 805, 811, 802, 804, 805, 814, 808, 808, 807, 801, 814, 799, 810, 808, 804, 797, 816, 805, 809, 803, 805, 805, 809, 810]

#a=[3085, 3106, 2977, 3004, 2931, 2944, 2952, 3043, 3015, 2943]

E=806
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
