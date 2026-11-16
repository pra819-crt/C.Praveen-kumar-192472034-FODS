
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Customer dataset
data = {
    'Annual_Spending': [1000, 1200, 1500, 8000, 8500,
                        9000, 3000, 3500, 4000, 9500],
    'Visits': [2, 3, 2, 10, 11, 12, 5, 6, 5, 13],
    'Purchases': [3, 4, 3, 15, 16, 18, 7, 8, 9, 20]
}

df = pd.DataFrame(data)

# Standardize data
scaler = StandardScaler()
X = scaler.fit_transform(df)

# Apply K-Means
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = model.fit_predict(X)

print("Customer Segmentation:")
print(df)

print("\nAverage Characteristics of Each Cluster:")
print(df.groupby('Cluster').mean().round(2))
