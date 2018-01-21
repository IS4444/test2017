import numpy as np
import matplotlib.pyplot as plt
import sys

B = 0.0
D = 0.0
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Y = []
n = 20
count = 0

print("Mode selection Default:1 Ramdaom:2 Exit:Other keys")
mode = input('>> ')

if mode == 1:
   Y = [200.0, 186.0, 164.0, 160.0, 148.0, 137.0, 134.0, 122.0, 113.0, 98.0, 89.0, 77.0, 71.0, 62.0, 49.0, 38.0, 30.0, 21.0, 12.0, 3.0]
elif mode == 2:
   while count < n:
      Y.append(np.random.rand())
      count += 1
else:
   sys.exit()

print(Y)

for i in range(n):
   B += (X[i]*X[i])
   D += (X[i]*Y[i])

C = sum(Y)
E = sum(X)

a = (n*D-C*E)/(n*B-E*E)
b = (B*C-D*E)/(n*B-E*E)

x = np.linspace(0,n,n + 1)
y = a*x + b

plt.plot(x,y, label = 'Least squares approximate expression')
plt.plot(X,Y,'o', label = 'Data')

plt.title('least squares method Graph')
plt.xlabel('X-Axis')
plt.text(0,0,"y = %f x + %f"% (a,b),fontsize=18)#2,5
plt.ylabel('Y-Axis')
plt.legend()

plt.show()
