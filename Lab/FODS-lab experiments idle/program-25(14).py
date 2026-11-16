
import pandas as pd

data = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Age': [25, 30, 25, 40, 30, 25, 35, 40, 30, 25]
}

customer_data = pd.DataFrame(data)

frequency = customer_data['Age'].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(frequency)
