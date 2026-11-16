
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Get flower measurements
sl = float(input("Sepal length: "))
sw = float(input("Sepal width: "))
pl = float(input("Petal length: "))
pw = float(input("Petal width: "))

# Predict species
flower = [[sl, sw, pl, pw]]
prediction = model.predict(flower)

print("Predicted Species:", iris.target_names[prediction[0]])
5.1
