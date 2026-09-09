import matplotlib.pyplot as plt
import numpy as np

# Sample data
a = 100*np.pi
x = np.linspace(0,10,1000)
print(x[1])
y = np.sin(a*x)
print(y[4])

# Create and display plot
plt.figure()
plt.plot(x, y)
plt.title("Sine Wave")
plt.show()
print(x[5])

print(x[0], x[99])
print(y[0], y[99])

