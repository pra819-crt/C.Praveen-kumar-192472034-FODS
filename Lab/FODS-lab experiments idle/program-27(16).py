
import pandas as pd

data = {
    'Review': [
        'Good product and good quality',
        'Excellent product quality',
        'Good service and fast delivery',
        'Excellent service'
    ]
}

df = pd.DataFrame(data)

words = ' '.join(df['Review']).lower().split()

frequency = pd.Series(words).value_counts()

print("Word Frequency Distribution:")
print(frequency)
