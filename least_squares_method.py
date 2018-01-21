import numpy as np
import matplotlib.pyplot as plt

B = 0.0
D = 0.0
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Y = [200, 186, 164, 160, 148, 137, 134, 122, 113, 98, 89, 77, 71, 62, 49, 38, 30, 21, 12, 3]
n = 20

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
plt.ylabel('Y-Axis')
plt.legend()

plt.show()
