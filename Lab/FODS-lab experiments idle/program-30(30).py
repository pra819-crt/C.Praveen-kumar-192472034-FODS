
from sklearn.tree import DecisionTreeRegressor, export_text

# Dataset: mileage (km), age (years)
X = [
    [10000, 1], [20000, 2], [30000, 3],
    [40000, 4], [50000, 5], [60000, 6],
    [70000, 7], [80000, 8], [15000, 1],
    [35000, 3], [55000, 5], [75000, 7]
]

# Car prices in rupees
y = [
    900000, 800000, 700000, 600000,
    500000, 400000, 300000, 200000,
    850000, 680000, 480000, 280000
]

# Train CART regression model
model = DecisionTreeRegressor(max_depth=3, random_state=42)
model.fit(X, y)

# Get new car details
mileage = float(input("Enter car mileage (km): "))
age = float(input("Enter car age (years): "))

# Predict price
prediction = model.predict([[mileage, age]])
print("\nPredicted Car Price: Rs.", prediction[0])

# Display decision path
tree_rules = export_text(
    model, feature_names=['Mileage', 'Age']
)

print("\nDecision Tree Rules:")
print(tree_rules)

# Display path for the new car
path = model.decision_path([[mileage, age]])
print("Decision Path Node IDs:")
print(path.indices)
