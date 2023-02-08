import networkx as nx
import numpy as np
import ant_path_func as apf
import time

n = 34
p = 0.1

se = [3409559, 7788783, 9157129, 1725171, 6667084, 9784760, 1404770, 2795190, 8401683, 7828343]
e = []
nrw = []
sle = []
sgd = []
fle = []
fgd = []

for j in range(10):
    seed = se[j]  # r.randint(1000000, 10000000)
    G = nx.erdos_renyi_graph(n, p, seed=seed)   # χρήση του γεννήτορα erdos-renyi για τυχαίους γράφους

    d = nx.shortest_path(G)     # εύρεση συντομοτερων μονοπατιών All-Pair Shortest Path
    max_len = 0
    for v in d:     # βρίσκω το κομβο που είναι αρχή για μονοπάτι με την μεγαλύτερη απόσταση
        l_k = list(d[v])[-1]  # last key, παιρνω το τελευταίο κόμβο γιατι τα αποτελέσματα διατάσονται σε αυξουσα απόσταση
        ln = d[v][l_k].__len__()    # length of path to last key
        if ln > max_len:
            max_len = ln
            s = v

    dijk = nx.single_source_dijkstra(G, s)    # dijkstra απο τον κόμβο που έπέλεξα σαν αρχή προς όλους τους άλλους
    t = list(dijk[0].keys())[-1]  # παρε το πιο απομακρισμενο κομβο για στοχο του αλγοριθμου

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

    se.append(seed)
    e.append(G.number_of_edges())
    nrw.append(num_rw)  # number of random walks
    sle.append(round(succ/10.0, 3))  # Loop erased success rate
    sgd.append(round(succ_gd/10.0, 3))  # Geodesic success rate
    fle.append(round(fail/10.0, 3))  # Loop erased fail rate
    fgd.append(round(fail_gd/10.0, 3))  # Geodesic fail rate

print(se, " # seeds")
print(e, " # number of edges")
print(nrw, " # number of random walks")
print(sle, " # Loop erased success rate")
print(sgd, " # Geodesic success rate")
print(fle, " # Loop erased fail rate")
print(fgd, " # Geodesic fail rate")
