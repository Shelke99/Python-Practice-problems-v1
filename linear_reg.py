import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample Data
data = {"Hours": [1, 2, 3, 4, 5], "Marks": [20, 40, 50, 60, 80]}
df = pd.DataFrame(data)
print(df)
# Separate input (X) and output (y)
X = df[["Hours"]]   # Input must be 2D
y = df["Marks"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Equation of line
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)

# Predict for 4.5 hours
prediction = model.predict([[4.5]])
print("Predicted Marks for 4.5 hours:", prediction[0])
