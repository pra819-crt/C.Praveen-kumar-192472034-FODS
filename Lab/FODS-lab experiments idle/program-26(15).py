
import pandas as pd

data = {
    'Post_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Likes': [100, 150, 100, 200, 150, 100, 250, 200, 150, 100]
}

posts = pd.DataFrame(data)

frequency = posts['Likes'].value_counts().sort_index()

print("Frequency Distribution of Likes:")
print(frequency)
