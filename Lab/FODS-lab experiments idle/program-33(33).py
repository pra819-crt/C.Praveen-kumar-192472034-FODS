
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Car dataset
data = {
    'Engine_Size': [1.0, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2, 2.5, 3.0],
    'Horsepower': [60, 75, 90, 100, 110, 130, 150, 170, 200, 250],
    'Mileage': [25, 23, 22, 21, 20, 18, 17, 16, 14, 12],
    'Price': [400000, 500000, 600000, 700000, 800000,
              1000000, 1200000, 1400000, 1800000, 2500000]
}

df = pd.DataFrame(data)

# Select features and target
X = df[['Engine_Size', 'Horsepower', 'Mileage']]
y = df['Price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict prices
y_pred = model.predict(X_test)

# Evaluate model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Display influential factors
print("\nFeature Coefficients:")
for feature, value in zip(X.columns, model.coef_):
    print(feature, ":", round(value, 2))

# Predict new car price
engine = float(input("\nEnter engine size: "))
hp = float(input("Enter horsepower: "))
mileage = float(input("Enter mileage (km/l): "))

new_car = pd.DataFrame({
    'Engine_Size': [engine],
    'Horsepower': [hp],
    'Mileage': [mileage]
})

price = model.predict(new_car)
print("Predicted Car Price: Rs.", round(price[0], 2))
