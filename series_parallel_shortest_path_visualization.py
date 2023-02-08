import networkx as nx
import ant_path_func as apf

sp = "v_series_parallel"
end = ".graphml"
nd = [10, 20, 40]

for i in range(3):
    fname = str(nd[i])+sp+end
    G = nx.read_graphml(fname, node_type=int)
    nx.set_edge_attributes(G, 0, name="use")
    num_run = 1
    num_rw = 3500  # αριθμός τυχαίων περιπάτων
    for v in G.nodes():
        if G.nodes[v]["type"] == "source":
            s = v
        elif G.nodes[v]["type"] == "terminal":
            t = v
    print("Dijkstra Shortest Path")
    dijk = nx.shortest_path(G, s, t)
    dj = zip(dijk[:-1], dijk[1:])
    for e in dj:
        G.edges[e]["use"] += 1
    res1 = 0
    while res1 != 1:
        print("LOOP ERASED PROCEDURE")
        [res1, res2] = apf.loop_erased_procedure(G, s, t, num_rw, num_run)  # αριθμός επιτυχημένων εκτελέσεων, Επιτυχημένη θεωρείται άν η αλγοριθμος μας βρεί μήκος μονοπατιού ίδιο με τον dijkstra
    a = apf.a_s_p(G, s, t)
    pth = zip(a[:-1], a[1:])
    for e in pth:
        G.edges[e]["use"] += 3
    res1 = 0
    while res1 != 1:
        print("GEODESIC PROCEDURE ")
        [res1, res2] = apf.geodesic_procedure(G, s, t, num_rw, num_run)  # αριθμός επιτυχημένων εκτελέσεων, Επιτυχημένη θεωρείται άν η αλγοριθμος μας βρεί μήκος μονοπατιού ίδιο με τον dijkstra
    a = apf.a_s_p(G, s, t)
    pth = zip(a[:-1], a[1:])
    for e in pth:
        G.edges[e]["use"] += 5
    fname = "series_parallel_"+str(nd[i])+"v_shortest_paths_vis.graphml"
    nx.write_graphml_lxml(G, fname)
