import matplotlib.pyplot as plt


# List of numbers from 1 to 1000 -- last number not included
x_values = list(range(1, 1001))
# List comprehension generates y-values
y_values = [x**2 for x in x_values]

# # Can color the scatter dots
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

# # For color can use RGB color model.
# # Values closer to 0 produce darker colors; closer to 1 produce lighter colors
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# Can use a color map & how to assign how to use it
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

# # Can show the plot
# plt.show()

# Or can save the plot as a figure automatically
# Saves in the same directory as py script, and 'tight' option trims extra whitespace
plt.savefig('squares_plot.png', bbox_inches='tight')

