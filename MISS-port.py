import numpy as np
import matplotlib.pyplot as plt

# Sigmoid easing function
def sigmoid_ease(x):
    return 1 / (1 + np.exp(-x))

# Generate data for the transition
x = np.linspace(-10, 10, 100)
y = sigmoid_ease(x)

# Plot the easing function
plt.plot(x, y)
plt.title('Sigmoid Easing Function')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.show()
