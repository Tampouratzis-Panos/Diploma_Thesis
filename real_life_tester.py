import networkx as nx
import numpy as np
import ant_path_func as apf
import time
import random as r


g1 = nx.read_graphml("airlines.graphml", node_type=int)
ri = r.randint(0, g1.number_of_nodes())
s = ri
ri = r.randint(0, g1.number_of_nodes())
t = ri
routes = [{s, t}]
while routes.__len__() < 10:
    ri = r.randint(0, g1.number_of_nodes())
    s = ri
    ri = r.randint(0, g1.number_of_nodes())
    t = ri
    if {s, t} not in routes:
        routes.append({s, t})

G = nx.Graph()
G.add_nodes_from(g1.nodes)
n = list(g1.nodes())[-1] + 1    # ευρεση μεγαλύτερου αναγνωριστικού κόμβου και αυξηση του κατα 1
for ee in g1.edges:
    if ee[2] != 0:   # ελεγχω αν η ακμή e έχει πολλαπλότητα διαφορετική του μηδενός
        G.add_node(n)
        G.add_edge(ee[0], n)     # ενθέτω τον κόμβο n ώστε η ακμή e να αντικασταθεί απο 2
        G.add_edge(ee[1], n)
        n += 1  # αυξανω το αναγνωριστικό του κόμβου
    else:
        G.add_edge(ee[0], ee[1])
print(G.number_of_edges())
e = [g1.number_of_edges(), G.number_of_edges()]
n = [g1.number_of_nodes(), G.number_of_nodes()]
nrw = []
sle = []
sgd = []
fle = []
fgd = []

print(e, " # edges original, no multi edges")
print(n, " # nodes original, no multi edges")
print(routes, " # routes")

for j in range(10):

    s = routes[j].pop()
    t = routes[j].pop()
    num_run = 10   # ποσες φορές θα εκτελεστεί
    i = 3  # αριθμός επαναληψεων απο το πειραμα για ρυθμο επιτυχιας ωστε να εχει καλή επιτυχια και να τελείωσει και γρήγορα
    num_rw = int(np.ceil(g1.number_of_edges()*(0.5+i**2)))  # αριθμός τυχαίων περιπάτων

    succ = 0
    fail = 0
    succ_gd = 0
    fail_gd = 0
    for i in range(10):
        t0 = time.time()
        print("LOOP ERASED PROCEDURE")
        [res1, res2] = apf.loop_erased_procedure(G, s, t, num_rw, num_run)  # αριθμός επιτυχημένων εκτελέσεων, Επιτυχημένη θεωρείται άν η αλγοριθμος μας βρεί μήκος μονοπατιού ίδιο με τον dijkstra
        succ += res1/num_run
        fail += res2/num_run
        print("GEODESIC PROCEDURE ")
        [res1, res2] = apf.geodesic_procedure(G, s, t, num_rw, num_run)  # αριθμός επιτυχημένων εκτελέσεων, Επιτυχημένη θεωρείται άν η αλγοριθμος μας βρεί μήκος μονοπατιού ίδιο με τον dijkstra
        succ_gd += res1/num_run
        fail_gd += res2/num_run
        t1 = time.time()
        print("Run", i, " Time ", t1 - t0, "s")
        print("")

    nrw.append(num_rw)  # number of random walks
    sle.append(round(succ/10.0, 3))  # Loop erased success rate
    sgd.append(round(succ_gd/10.0, 3))  # Geodesic success rate
    fle.append(round(fail/10.0, 3))  # Loop erased fail rate
    fgd.append(round(fail_gd/10.0, 3))  # Geodesic fail rate

print(e, " # number of edges")
print(n, " # number of nodes")
print(nrw, " # number of random walks")
print(sle, " # Loop erased success rate")
print(sgd, " # Geodesic success rate")
print(fle, " # Loop erased fail rate")
print(fgd, " # Geodesic fail rate")
