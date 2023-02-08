import matplotlib.pyplot as plt

x = [3, 8, 23, 48, 83, 128, 183, 248, 323, 408]  # number of random walks
yle = [0.75, 0.9, 1.0, 0.95, 1.0, 0.95, 1.0, 1.0, 1.0, 1.0]  # Loop erased success rate
ygd = [0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]  # Geodesic success rate

# line 1 points
# plotting the line 1 points
plt.plot(x, yle, 's-b', label="Loop Erased")
# plotting the line 2 points
plt.plot(x, ygd, '1--r', label="Geodesic")
# naming the x axis
plt.xlabel('Number of Random Walks')
# naming the y axis
plt.ylabel('Success Rate')
# giving a title to my graph
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=4, #E=5')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()
