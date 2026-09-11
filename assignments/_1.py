import matplotlib.pyplot as plt
import numpy as np
import math

# Sample data
n = 100
a = 0
b = 1
deltax = (b-a)/n
area = 0.0

x = np.linspace(0,10,n)
y = np.linspace(0,0,n)

# # Exponential e^x
# for i in range(n):
#     y[i] = math.exp(x[i])

# # Parabola x^2
# for i in range(n):
#     y[i] = x[i]**2

# # Integrate
# for i in range(n):
#     area += deltax * y[i]

# print(area)

# Create and display plot
plt.figure()
plt.plot(x, y)
plt.title("parabola")
plt.show()


