import matplotlib.pyplot as plt


# List of numbers from 1 to 1000 -- last number not included
x_values = list(range(1, 1001))
# List comprehension generates y-values
y_values = [x**2 for x in x_values]

# For color can use RGB color model.
# Values closer to 0 produce darker colors; closer to 1 produce lighter colors
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()

