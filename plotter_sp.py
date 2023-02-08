import matplotlib.pyplot as plt

# 10v
x = [7, 21, 63, 133, 231, 357, 511, 693, 903, 1141]  # Number of random walks
yle = [0.6, 0.5, 0.8, 0.85, 0.9, 0.95, 0.95, 1.0, 0.95, 1.0]  # Loop erased success rate
ygd = [0.05, 0.6, 0.7, 0.85, 0.95, 0.95, 0.95, 0.9, 1.0, 1.0]  # Geodesic success rate

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
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=10, #E=14')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

# 20v
x = [26, 78, 234, 494, 858, 1326, 1898, 2574, 3354, 4238]  # Number of random walks
yle = [0.4, 0.7, 0.85, 0.9, 0.95, 1.0, 0.95, 1.0, 1.0, 0.9]  # Loop erased success rate
ygd = [0.15, 0.65, 1.0, 0.85, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0]  # Geodesic success rate

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
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=34, #E=52')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

# 40v
x = [103, 308, 923, 1948, 3383, 5228, 7483, 10148, 13223, 16708]  # Number of random walks
yle = [0.15, 0.45, 0.8, 0.85, 1.0, 1.0, 0.95, 0.95, 1.0, 1.0]  # Loop erased success rate
ygd = [0.2, 0.65, 0.7, 0.95, 0.95, 1.0, 0.95, 0.95, 1.0, 1.0]  # Geodesic success rate

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
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=128, #E=205')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()
