
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Customer transaction dataset
data = {
    'Customer_ID': [101, 102, 103, 104, 105,
                    106, 107, 108, 109, 110],
    'Amount_Spent': [1000, 1500, 1200, 8000, 9000,
                     8500, 3000, 3500, 4000, 9500],
    'Visits': [2, 3, 2, 10, 12, 11, 5, 6, 5, 13]
}

df = pd.DataFrame(data)

# Select features
X = df[['Amount_Spent', 'Visits']]

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Segment'] = model.fit_predict(X_scaled)

# Display results
print("Customer Segmentation:")
print(df)

print("\nAverage Spending and Visits by Segment:")
print(df.groupby('Segment')[['Amount_Spent', 'Visits']].mean().round(2))
