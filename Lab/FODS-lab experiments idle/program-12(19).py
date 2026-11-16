
import pandas as pd
from scipy import stats

df = pd.read_csv("drug_placebo_data.csv")

for col in df.columns:
    data = df[col].dropna()
    mean = data.mean()
    se = stats.sem(data)
    ci = stats.t.interval(
        0.95, len(data)-1,
        loc=mean, scale=se
    )
    print(col, "Mean:", round(mean, 2))
    print("95% CI:", ci)
