
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'Customer_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Amount_Spent': [1000, 1200, 1500, 5000, 5500,
                     6000, 9000, 9500, 10000],
    'Items_Purchased': [2, 3, 3, 8, 9, 10, 15, 16, 18]
}

df = pd.DataFrame(data)

X = df[['Amount_Spent', 'Items_Purchased']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = model.fit_predict(X_scaled)

print("Customer Segments:")
print(df)

plt.scatter(df['Amount_Spent'], df['Items_Purchased'],
            c=df['Cluster'])
plt.xlabel("Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Segmentation using K-Means")
plt.show()
