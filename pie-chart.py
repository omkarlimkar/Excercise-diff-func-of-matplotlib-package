import matplotlib.pyplot as plt

# Sample data
sizes = [30, 25, 15, 10, 20]
labels = ['A', 'B', 'C', 'D', 'E']

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Add title
plt.title('Pie Chart')

# Display the plot
plt.show()
