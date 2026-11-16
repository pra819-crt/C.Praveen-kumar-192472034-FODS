
import pandas as pd
import numpy as np
from scipy.stats import t

df = pd.read_csv("customer_reviews.csv")

ratings = df["rating"].dropna()

n = len(ratings)
mean = ratings.mean()
std = ratings.std()
se = std / np.sqrt(n)

t_value = t.ppf(0.975, n - 1)

lower = mean - t_value * se
upper = mean + t_value * se

print("Mean Rating:", round(mean, 2))
print("95% Confidence Interval:")
print("Lower Limit:", round(lower, 2))
print("Upper Limit:", round(upper, 2))
