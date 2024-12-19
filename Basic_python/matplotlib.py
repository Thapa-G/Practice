import matplotlib.pyplot as plt  

# Data for the first line
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Data for the second line
x1 = [6, 7, 8, 9, 10]
y1 = [2, 3, 5, 7, 11]

# Plotting the first line
plt.plot(x, y, marker='o', linestyle='--', color='b', label='prime number')

# Plotting the second line
plt.plot(x1, y1, marker='o', linestyle='-', color='r', label='line2')

# Adding labels and title
plt.xlabel('X axis')  # Corrected
plt.ylabel('Y axis')  # Corrected
plt.title('Prime Numbers')

# Adding the legend
plt.legend()

# Displaying the plot
plt.show()
