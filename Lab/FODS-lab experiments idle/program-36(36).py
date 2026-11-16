
import pandas as pd

# Create stock dataset
data = {
    'Date': ['01-01', '02-01', '03-01', '04-01', '05-01',
             '06-01', '07-01', '08-01'],
    'Close': [150, 155, 148, 160, 165, 158, 170, 175]
}

df = pd.DataFrame(data)
df.to_csv('stock_data.csv', index=False)

# Read CSV file
df = pd.read_csv('stock_data.csv')

prices = df['Close']

print("Stock Data:")
print(df)

print("\nMean Price:", prices.mean())
print("Variance:", prices.var())
print("Standard Deviation:", prices.std())
print("Minimum Price:", prices.min())
print("Maximum Price:", prices.max())
print("Price Range:", prices.max() - prices.min())

if prices.std() < 10:
    print("Insight: Stock prices are relatively stable.")
else:
    print("Insight: Stock prices show high variability.")
