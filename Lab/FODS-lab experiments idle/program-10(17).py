import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

df = pd.read_csv("data.csv")
stop = {"the", "is", "and", "a", "to", "of"}
words = []

for text in df["feedback"].dropna():
    text = re.sub(r"[^\w\s]", "", text.lower())
    words.extend(w for w in text.split() if w not in stop)

n = int(input("Enter top N: "))
top = Counter(words).most_common(n)

print(top)

if top:
    w, c = zip(*top)
    plt.bar(w, c)
    plt.show()
