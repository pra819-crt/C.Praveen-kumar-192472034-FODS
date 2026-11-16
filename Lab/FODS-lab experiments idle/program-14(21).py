
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("rare_elements.csv")
data = df["concentration"]

n = int(input("Enter sample size: "))
level = float(input("Enter confidence level (%): "))
precision = float(input("Enter desired precision: "))

sample = data.head(n)
mean = np.mean(sample)
se = stats.sem(sample)
alpha = 1 - level / 100

ci = stats.t.interval(
    level / 100, len(sample) - 1,
    loc=mean, scale=se
)

print("Sample mean:", round(mean, 3))
print("Confidence interval:", ci)
print("Margin of error:", round((ci[1] - ci[0]) / 2, 3))

if (ci[1] - ci[0]) / 2 <= precision:
    print("Desired precision achieved")
else:
    print("Desired precision not achieved")
