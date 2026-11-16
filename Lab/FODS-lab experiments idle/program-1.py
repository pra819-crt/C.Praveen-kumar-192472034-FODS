
import numpy as np

marks = np.array([
    [85, 78, 90, 82],
    [75, 88, 84, 79],
    [92, 81, 89, 85],
    [80, 90, 86, 88]
])

subjects = ["Math", "Science", "English", "History"]
avg = np.mean(marks, axis=0)

for s, a in zip(subjects, avg):
    print(s, ":", a)

print("Highest average:", subjects[np.argmax(avg)])
