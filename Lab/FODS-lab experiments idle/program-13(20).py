
import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("ab_test.csv")

t, p = ttest_ind(df["design_A"], df["design_B"])

print("P-value:", round(p, 4))

if p < 0.05:
    print("Significant difference exists")
else:
    print("No significant difference")
