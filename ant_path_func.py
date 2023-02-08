import numpy
import networkx as nx


def random_walk(graph, start, finish):
    """Performs random walk from Nest to Food
    returns graph with edges that agent traversed"""
    g = graph   # input graph
    n = start   # Start node, the nest
    wg = nx.Graph()  # output graph with all the edges that have been traversed in the random walk
    wg.add_node(n)   # Start node for the new graph
    step = 0    # number of steps taken during the walk. it's used in the Loop-Erased Procedure to identify the earliest traversed edge when needed

    while n != finish:  # n is the node the walker is at currently
        nbrs = g.neighbors(n)  # object with neighbors on node the agent is at currently
        sum_pher = 0    # sum of pheromone on adjacent edges

        for v in nbrs:  # for loop summing pheromone on adjacent edges
            sum_pher += g.edges[n, v]['pheromone']

        p = numpy.random.uniform(0.0, 1.0)  # random number generation to simulate randomness in edge selection

        nbrs = g.neighbors(n)   # object with neighbors on node the agent is currently
        for v in nbrs:
            prob = g.edges[n, v]['pheromone']/sum_pher  # probability of choosing edge (n,v)
            if prob > p:
                g.nodes[v]['prev'] = n  # noting the node from where v was reached
                if not wg.has_node(v):
                    wg.add_node(v)  # adding chosen node v to output graph
                    wg.add_edge(n, v, step=step)  # add edge from current node n to chosen node v
                n = v  # assigning to n the chosen node v
                step += 1
                break
            else:
                p = p - prob  # decreasing the random number so it becomes smaller than the probability of some other edge
        if n == start:  # if the agent has reached the start node again we reinitialize the random walk
            wg = nx.Graph()
            wg.add_node(n)
            step = 0
    return wg


def loop_erasure(graph, nest, food):
    """Creates the loop erased path the agent followed return graph of used edges """

    leg = nx.Graph()    # Output Graph with only the loop erased path
    n = food    # this process starts from the last node, food

    while n != nest:    # looking to reach the nest, start node, n is current node
        min_step = float('inf')  # initializing the earliest step to inf
        for e in graph.edges(n):    # Looping through the edges adjacent to n
            es = graph.edges[e]['step']
            if es < min_step:   # if the step value of edge e is lower than the earliest step
                min_step = es   # change the value of the earliest step
                next_node = e[1]    # keep the value of the node connected to node n via edge e
        leg.add_edge(n, next_node)  # add selected edge to output graph
        n = next_node   # change current node
    return leg

def a_s_p(graph, nest, food):
    """Get the path with most pheromone ant_shortest_path"""
    g = graph   # input graph
    v = nest    # start node
    path = [v]  # array storing the path

    while v != food:    # stop when reaching the food node
        mx = 0  # maximum pheromone value of adjecent edges
        mx_v = v    # node connected to edge with max pheromone
        for e in g.edges(v):    # looping through edges adjacent to v
            ph = g.edges[e]['pheromone']
            if mx < ph and not(e[1] in path):   # check if pheromone level is greater than the max value and the other connected node is not already in the path to stop looping back
                mx = ph
                mx_v = e[1]
        if mx_v in path:
            path = [v]
            break
        path.append(mx_v)   # add node connected to edge with max pheromone to the path
        v = mx_v    # change current node

    return path


def loop_erased_procedure(G, s, food, num_rw, num_run):
    succ = 0
    fail = 0
    dijk = nx.single_source_dijkstra(G, s, target=food)
    for j in range(num_run):
        for e in G.edges:   # Αρχικοποίηση επιπέδου φερομόνης στην άρχη κάθε κύκλου
            G.edges[e]['pheromone'] = 1
        for i in range(num_rw):    # εκτέλεση τυχαιου περίπατου και loop-erasure
            walk = random_walk(G, s, food)
            le_path = loop_erasure(walk, s, food)
            for e in le_path.edges: # για ακμές που είναι στο επιλεγμένο μονοπάτι αυξάνω την φερομόνη
                G.edges[e]['pheromone'] += 1
        sol = a_s_p(G, s, food)     # βρίσκω το μονοπάτι με την περισσότερη φερομόνη
        if dijk[1].__len__() == sol.__len__():  # συγκρίνω αριθμό κόμβων
            succ += 1
        elif 1 == sol.__len__():
            fail += 1
        if (j+1) % 20 == 0:   # για να ξερουμε αν τρέχει σε κάποια σημεία κολλάει
            print(":")
        else:
            print(":", end="")

    return succ, fail

def geodesic_procedure(G, s, food, num_rw, num_run):

    dijk = nx.single_source_dijkstra(G, s, target=food)
    succ_gd = 0
    fail = 0
    for j in range(num_run):
        for e in G.edges:   # Αρχικοποίηση επιπέδου φερομόνης
            G.edges[e]['pheromone'] = 1
        for i in range(num_rw):
            walk_gd = random_walk(G, s, food)   # εκτέλεση τυχαίου περιπάτου
            walk_sp = nx.shortest_path(walk_gd, s, food)    # ευρεση συντομότερης διαδρομής στον γράφο που δημιουργείται απο τον περίπατο,
            edge_sp = zip(walk_sp[:-1], walk_sp[1:])    # δημιουργία των ακμών της συντομότερης διαδρομής
            for k in edge_sp:   # αυξηση φερομονης συντομοτερης διαδρομής
                G.edges[k]['pheromone'] += 1
        sol = a_s_p(G, s, food)      # βρίσκω το μονοπάτι με την περισσότερη φερομόνη
        if dijk[1].__len__() == sol.__len__():
            succ_gd += 1
        elif 1 == sol.__len__():
            fail += 1
        if (j+1)%20 == 0:
            print(".")
        else:
            print(".", end="")

    return succ_gd, fail
