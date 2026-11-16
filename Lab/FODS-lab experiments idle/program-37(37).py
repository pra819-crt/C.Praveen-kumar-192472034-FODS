
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Exam_Score': [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

correlation = df['Study_Hours'].corr(df['Exam_Score'])

print("Correlation:", correlation)

if correlation > 0:
    print("Positive Correlation")
elif correlation < 0:
    print("Negative Correlation")
else:
    print("No Correlation")

plt.scatter(df['Study_Hours'], df['Exam_Score'])
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Time vs Exam Scores")
plt.grid()
plt.show()

plt.plot(df['Study_Hours'], df['Exam_Score'], marker='o')
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Time and Exam Scores")
plt.grid()
plt.show()
