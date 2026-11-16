
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Create house dataset
data = {
    'Size': [800, 1000, 1200, 1500, 1800,
             2000, 2200, 2500, 2800, 3000],
    'Price': [2000000, 2500000, 3000000, 3800000, 4500000,
              5000000, 5500000, 6200000, 7000000, 7500000]
}

df = pd.DataFrame(data)

# Bivariate analysis
plt.scatter(df['Size'], df['Price'])
plt.xlabel("House Size (sq.ft)")
plt.ylabel("House Price (Rs.)")
plt.title("House Size vs House Price")
plt.show()

# Split data
X = df[['Size']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Predict new house price
size = float(input("Enter house size (sq.ft): "))
price = model.predict(pd.DataFrame({'Size': [size]}))

print("Predicted House Price: Rs.", round(price[0], 2))
