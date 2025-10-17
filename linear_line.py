import matplotlib.pyplot as plt
import numpy as np

# Example data (Hours vs Marks)
hours = np.array([1, 2, 3, 4, 5])
marks = np.array([20, 40, 50, 60, 80])

# Fit a line (using numpy polyfit for simplicity)
m, c = np.polyfit(hours, marks, 1)
line = m * hours + c

# Plot scatter + regression line
plt.figure(figsize=(7,5))
plt.scatter(hours, marks, color="blue", label="Data Points")
plt.plot(hours, line, color="red", label=f"Best Fit Line: y={m:.2f}x+{c:.2f}")
plt.xlabel("Hours of Study")
plt.ylabel("Marks Scored")
plt.title("Linear Regression: Hours vs Marks")
plt.legend()
plt.grid(True)