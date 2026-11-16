
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Training data: Fever, Cough, Fatigue
X = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
])

# 0 = No condition, 1 = Condition
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

k = int(input("Enter number of neighbors (K): "))

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

fever = int(input("Fever (0/1): "))
cough = int(input("Cough (0/1): "))
fatigue = int(input("Fatigue (0/1): "))

patient = np.array([[fever, cough, fatigue]])

prediction = model.predict(patient)

if prediction[0] == 1:
    print("Patient has a medical condition")
else:
    print("Patient does not have a medical condition")
