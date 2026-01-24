import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

mileage = np.array([5000, 6000, 8000, 10000, 12000, 15000, 18000, 20000, 22000, 25000])
price = np.array([25000, 24000, 22000, 20000, 18000, 16000, 15000, 14000, 13000, 12000])

mileage = mileage.reshape(-1, 1)
price = price.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(mileage, price, test_size=0.3, random_state=42)
print("x_train is : ", X_train)
print("x_test is : ", X_test)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

r_squared = model.score(X_test, y_test)

print("Coefficient of determination (R^2):", r_squared)
plt.plot(mileage, price)
plt.show()