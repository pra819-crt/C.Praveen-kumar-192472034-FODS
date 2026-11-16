
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 150, 100, 180, 200, 170]

# Line plot
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# Scatter plot
plt.scatter(months, sales)
plt.title("Monthly Sales - Scatter Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# Bar plot
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
