import networkx as nx
import matplotlib.pyplot as plt
import random as r

seed = r.randint(1000000, 10000000)

n = 10  # αριθμός κόμβων
p = 0.4  # πιθανότητα εμφάνισης τριγώνου/ υπάρξης ακμής powerlaw/ erdos-renyi αντιστοιχα

#G = nx.erdos_renyi_graph(n, p, seed=seed)   # χρήση του γεννήτορα erdos-renyi για τυχαίους γράφους
G = nx.powerlaw_cluster_graph(n, 2, p=p, seed=seed)   # χρήση του γεννήτορα erdos-renyi για τυχαίους γράφους
if nx.is_connected(G):
    print("G is all one graph")
d = nx.shortest_path(G)     # εύρεση συντομοτερων μονοπατιών All-Pair Shortest Path
print("number of edges ", G.number_of_edges())

max_len = 0
for v in d:     # βρίσκω το κομβο που είναι αρχή για μονοπάτι με την μεγαλύτερη απόσταση
    l_k = list(d[v])[-1]  # last key, παιρνω το τελευταίο κόμβο γιατι τα αποτελέσματα διατάσονται σε αυξουσα απόσταση
    ln = d[v][l_k].__len__()    # length of path to last key
    if ln > max_len:
        max_len = ln
        s = v

dijk = nx.single_source_dijkstra(G, s)    # dijkstra απο τον κόμβο που έπέλεξα σαν αρχή προς όλους τους άλλους
t = list(dijk[0].keys())[-1]  # παρε το πιο απομακρισμενο κομβο για στοχο του αλγοριθμου
nx.set_node_attributes(G, "node", name="kind")
G.nodes[t]["kind"] = "terminal"
G.nodes[s]["kind"] = "source"
nx.write_graphml_lxml(G, ".graphml")  # ονομα αρχείου γράφου
print(G.degree())

pos = nx.nx_agraph.graphviz_layout(G, prog="dot", args="")
labels = nx.get_node_attributes(G, 'kind')
nx.draw(G, pos=pos, with_labels=True, labels=labels)
nx.draw(G, pos=pos, nodelist=[s], node_color="tab:red")
nx.draw(G, pos=pos, nodelist=[t], node_color="tab:green")
plt.show()

print("seed =", seed)
