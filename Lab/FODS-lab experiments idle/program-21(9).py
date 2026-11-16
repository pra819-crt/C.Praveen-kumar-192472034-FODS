
import pandas as pd

property_data = pd.DataFrame({
    'Property_ID': [101, 102, 103, 104, 105],
    'Location': ['Chennai', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai'],
    'Bedrooms': [3, 5, 4, 6, 2],
    'Area': [1200, 1800, 1500, 2200, 1000],
    'Price': [5000000, 8000000, 6500000, 9000000, 4000000]
})

print("Average listing price by location:")
print(property_data.groupby('Location')['Price'].mean())

print("\nProperties with more than 4 bedrooms:")
print(len(property_data[property_data['Bedrooms'] > 4]))

print("\nProperty with the largest area:")
print(property_data.loc[property_data['Area'].idxmax()])
