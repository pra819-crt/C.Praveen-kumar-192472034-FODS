
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("age_body_fat.csv")

print(df.describe().loc[["mean", "50%", "std"]])

df[["age", "fat"]].plot(
    kind="box", subplots=True, layout=(1, 2)
)
plt.show()

plt.scatter(df["age"], df["fat"])
plt.xlabel("Age")
plt.ylabel("Body Fat (%)")
plt.show()

stats.probplot(df["age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()

stats.probplot(df["fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat")
plt.show()
