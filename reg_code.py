import matplotlib.pyplot as plt
import numpy as np

# Given data (from image)
x = np.array([8, 10, 12])  # Diameter in inches
y = np.array([10, 13, 16])  # Price in dollars

# Calculate mean values
mean_x = np.mean(x)
mean_y = np.mean(y)

# Calculate slope (m) and intercept (b) using formulas
m = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x)**2)
b = mean_y - (m * mean_x)

# Generate regression line
y_pred = m * x + b  

# Plot data points and regression line
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x, y_pred, color='blue', label=f'Regression Line: y = {m:.2f}x + {b:.2f}')
plt.xlabel('Diameter (in inches)')
plt.ylabel('Price (in dollars)')
plt.title('Linear Regression: Pizza Diameter vs Price')
plt.legend()
plt.grid(True)
plt.show()
