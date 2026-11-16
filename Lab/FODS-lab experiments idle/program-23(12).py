
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temperature = [25, 27, 30, 33, 35, 34, 32, 31, 30, 28, 26, 24]
rainfall = [20, 15, 25, 40, 60, 120, 180, 160, 140, 90, 50, 30]

# Line plot for temperature
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.show()

# Scatter plot for rainfall
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.show()
