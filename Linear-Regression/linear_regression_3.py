import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([30, 35, 50, 55, 65, 70, 75])

x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
m = numerator / denominator
b = y_mean - m * x_mean

y_pred = m * x + b

mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print(" Model Evaluation:")
print(f" Slope (m): {m:.2f}")
print(f" Intercept (b): {b:.2f}")
print(f" R-squared: {r2:.4f}")
print(f" MAE: {mae:.2f}")
print(f" MSE: {mse:.2f}")
print(f" RMSE: {rmse:.2f}")

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.title("Linear Regression Fit")
plt.legend()
plt.grid(True)