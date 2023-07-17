import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3, 4, 5]  # x-coordinates
y = [2, 4, 6, 8, 10]  # y-coordinates

# Plotting the dots
plt.scatter(x, y)

# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Dot Graph')

# Display the graph
plt.show()
