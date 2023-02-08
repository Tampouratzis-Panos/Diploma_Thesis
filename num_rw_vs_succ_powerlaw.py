import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import ant_path_func as apf
import sp_func as a
import time


#G = nx.read_graphml("10v_powerlaw.graphml", node_type=int)
#G = nx.read_graphml("20v_powerlaw.graphml", node_type=int)
G = nx.read_graphml("40v_powerlaw.graphml", node_type=int)

print("edges", G.number_of_edges())

for v in G.nodes():
    if G.nodes[v]["kind"] == "source":
        s = v
    elif G.nodes[v]["kind"] == "terminal":
        t = v

num_run = 20   # ποσες φορές θα εκτελεστεί
num_rw = []  # αριθμός τυχαίων περιπάτων


succ = []
fail = []
succ_gd = []
fail_gd = []
for i in range(15):
    num_rw.append(int(np.ceil(G.number_of_edges()*(0.5+i**2))))
    t0 = time.time()
    print("LOOP ERASED PROCEDURE")
    [res1, res2] = apf.loop_erased_procedure(G, s, t, num_rw[i], num_run)  # αριθμός επιτυχημένων εκτελέσεων, Επιτυχημένη θεωρείται άν η αλγοριθμος μας βρεί μήκος μονοπατιού ίδιο με τον dijkstra
    succ.append(res1/num_run)
    fail.append(res2/num_run)
    print("GEODESIC PROCEDURE ")
    [res1, res2] = apf.geodesic_procedure(G, s, t, num_rw[i], num_run)  # αριθμός επιτυχημένων εκτελέσεων, Επιτυχημένη θεωρείται άν η αλγοριθμος μας βρεί μήκος μονοπατιού ίδιο με τον dijkstra
    succ_gd.append(res1/num_run)
    fail_gd.append(res2/num_run)
    t1 = time.time()
    print("Run", i, " Time ", t1 - t0, "s")
    print("")

print(num_rw, " # number of random walks")
print(succ, " # Loop erased success rate")
print(succ_gd, " # Geodesic success rate")
print(fail, " # Loop erased fail rate")
print(fail_gd, " # Geodesic success rate")
