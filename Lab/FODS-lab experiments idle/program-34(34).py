
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Patient dataset
data = {
    'Age': [25, 30, 45, 50, 35, 60, 40, 55, 28, 48,
            32, 65, 42, 52, 38, 58, 27, 62, 46, 34],
    'Gender': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
               1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'BP': [120, 140, 150, 160, 125, 170, 135, 165, 118, 155,
           130, 175, 145, 158, 128, 168, 122, 172, 148, 132],
    'Cholesterol': [180, 220, 240, 260, 190, 280, 210, 270, 175, 250,
                    195, 290, 230, 255, 200, 275, 185, 285, 235, 205],
    'Outcome': ['Good', 'Bad', 'Bad', 'Bad', 'Good',
                'Bad', 'Good', 'Bad', 'Good', 'Bad',
                'Good', 'Bad', 'Bad', 'Bad', 'Good',
                'Bad', 'Good', 'Bad', 'Bad', 'Good']
}

df = pd.DataFrame(data)

# Separate features and target
X = df[['Age', 'Gender', 'BP', 'Cholesterol']]
y = df['Outcome']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Display predictions
print("Actual and Predicted Outcomes:")
print(pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': y_pred
}))

# Evaluate model
print("\nModel Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, pos_label='Good'))
print("Recall:", recall_score(y_test, y_pred, pos_label='Good'))
print("F1-Score:", f1_score(y_test, y_pred, pos_label='Good'))
