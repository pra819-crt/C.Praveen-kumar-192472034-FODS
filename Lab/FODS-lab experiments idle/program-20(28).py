
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("customer_segments.csv")

X = data[["annual_spending", "items_purchased"]]

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means
model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X_scaled)

# Get new customer details
spending = float(input("Enter annual spending: "))
items = int(input("Enter items purchased: "))

customer = [[spending, items]]
customer_scaled = scaler.transform(customer)

segment = model.predict(customer_scaled)

print("Customer belongs to Segment:", segment[0] + 1)
