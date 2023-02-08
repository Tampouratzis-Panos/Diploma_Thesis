import matplotlib.pyplot as plt

# 10v
x = [9, 27, 81, 171, 297, 459, 657, 891, 1161, 1467]  # number of random walks
yle = [0.4, 0.45, 0.6, 0.7, 0.8, 0.9, 0.7, 0.9, 0.95, 1.0]  # Loop erased success rate
ygd = [0.3, 0.6, 0.7, 0.75, 0.75, 0.9, 0.85, 0.85, 0.95, 0.9]  # Geodesic success rate

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
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=10, #E=18')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

# 20v
x = [35, 104, 311, 656, 1139, 1760, 2519, 3416, 4451, 5624]  # number of random walks
yle = [0.65, 0.75, 0.95, 0.95, 1.0, 1.0, 0.95, 0.95, 1.0, 1.0]  # Loop erased success rate
ygd = [0.4, 0.85, 0.75, 0.95, 0.95, 0.95, 1.0, 1.0, 1.0, 1.0]  # Geodesic success rate

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
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=34, #E=69')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

# 40v
x = [107, 321, 963, 2033, 3531, 5457, 7811, 10593, 13803, 17441]  # number of random walks
yle = [0.35, 0.55, 0.65, 0.85, 0.95, 0.9, 0.95, 0.95, 0.95, 0.9]  # Loop erased success rate
ygd = [0.3, 0.6, 0.75, 0.9, 1.0, 0.9, 0.9, 1.0, 0.9, 0.9]  # Geodesic success rate

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
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=128, #E=214')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()
