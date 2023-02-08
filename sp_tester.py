import networkx as nx
import numpy as np
import ant_path_func as apf
import time

e = []
n = []
nrw = []
sle = []
sgd = []
fle = []
fgd = []
name = "sp_graph_"
end = ".graphml"

for j in range(10):
    fname = name+str(j)+end
    G = nx.read_graphml(fname, node_type=int)   # χρήση του γεννήτορα erdos-renyi για τυχαίους γράφους
    for v in G.nodes():
        if G.nodes[v]["kind"] == "source":
            s = v
        elif G.nodes[v]["kind"] == "terminal":
            t = v

    num_run = 10   # ποσες φορές θα εκτελεστεί
    i = 4  # αριθμός επαναληψεων απο το πειραμα για ρυθμο επιτυχιας ωστε να εχει καλή επιτυχια και να τελείωσει και γρήγορα
    num_rw = int(np.ceil(G.number_of_edges()*(0.5+i**2)))  # αριθμός τυχαίων περιπάτων

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

    e.append(G.number_of_edges())
    n.append(G.number_of_nodes())
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
