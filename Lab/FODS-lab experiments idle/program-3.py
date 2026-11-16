
import numpy as np

house_data = np.array([
    [3, 1200, 200000],
    [5, 1800, 350000],
    [4, 1500, 280000],
    [6, 2200, 450000],
    [5, 2000, 400000]
])

prices = house_data[house_data[:, 0] > 4, 2]

print("Average Sale Price:", np.mean(prices))
