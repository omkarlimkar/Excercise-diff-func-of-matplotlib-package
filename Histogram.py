import matplotlib.pyplot as plt

# Sample data
data = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5]

# Create a histogram
plt.hist(data, bins=5)

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')

# Display the plot
plt.show()
