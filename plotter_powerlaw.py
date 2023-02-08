import matplotlib.pyplot as plt

# 10v
x = [8, 24, 72, 152, 264, 408, 584, 792, 1032, 1304]   #  number of random walks
yle = [0.65, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]   #  Loop erased success rate
ygd = [0.75, 0.8, 0.85, 0.95, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]   # Geodesic success rate

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
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=10, #E=16')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

# 20v
x = [32, 96, 288, 608, 1056, 1632, 2336, 3168, 4128, 5216] # number of random walks
yle = [0.5, 0.8, 0.95, 0.95, 0.95, 1.0, 1.0, 0.9, 1.0, 1.0] # Loop erased success rate
ygd = [0.55, 0.85, 0.9, 1.0, 1.0, 0.95, 0.95, 1.0, 1.0, 1.0] # Geodesic success rate

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
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=34, #E=64')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

# 40v
x = [126, 378, 1134, 2394, 4158, 6426, 9198, 12474, 16254, 20538, 25326, 30618, 36414, 42714, 49518]  # number of random walks
yle = [0.45, 0.65, 0.55, 0.8, 0.55, 0.75, 0.85, 0.85, 0.75, 0.65, 0.75, 0.8, 0.7, 0.95, 0.8]  # Loop erased success rate
ygd = [0.45, 0.4, 0.6, 0.75, 0.75, 0.6, 0.8, 0.8, 0.75, 0.9, 0.75, 0.65, 0.85, 0.8, 0.65]  # Geodesic success rate
fle = [0.2, 0.0, 0.1, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # Loop erased fail rate
fgd = [0.05, 0.2, 0.05, 0.0, 0.05, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # Geodesic success rate

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
plt.title('Success Rate vs Number of Random Walks, num_run = 20, #V=128, #E=252')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()


# line 1 points
# plotting the line 1 points
plt.plot(x, fle, 'sb', label="Loop Erased")
# plotting the line 2 points
plt.plot(x, fgd, '1r', label="Geodesic")
# naming the x axis
plt.xlabel('Number of Random Walks')
# naming the y axis
plt.ylabel('Success Rate')
# giving a title to my graph
plt.title('Abort Rate vs Number of Random Walks, num_run = 20, #V=128, #E=252')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()
