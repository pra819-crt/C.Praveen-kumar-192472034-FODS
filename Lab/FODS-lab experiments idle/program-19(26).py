
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("housing_data.csv")

X = data[["area_sqft", "bedrooms"]]
y = data["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Get new house details
area = float(input("Enter house area (sq.ft): "))
bedrooms = int(input("Enter number of bedrooms: "))

# Predict price
price = model.predict([[area, bedrooms]])

print("Predicted House Price: Rs.", round(price[0], 2))
