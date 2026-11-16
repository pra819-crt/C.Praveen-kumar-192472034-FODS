
import pandas as pd

data = {
    'Chennai': [30, 32, 35, 34, 31, 33],
    'Delhi': [15, 20, 30, 38, 35, 18],
    'Bangalore': [22, 24, 25, 23, 24, 22]
}

df = pd.DataFrame(data)

print("Temperature Data:")
print(df)

print("\nMean Temperature:")
print(df.mean())

print("\nStandard Deviation:")
print(df.std())

temp_range = df.max() - df.min()

print("\nTemperature Range:")
print(temp_range)

print("\nHighest Temperature Range:",
      temp_range.idxmax())

print("Most Consistent City:",
      df.std().idxmin())
