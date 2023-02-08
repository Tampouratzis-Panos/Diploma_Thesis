import networkx as nx
import matplotlib.pyplot as plt
import sp_func as sp


m = 128
[sp_gr, lr] = sp.sp_generator(m, 's')    # δημιουργία δεντρου ακμών series-parallel γραφου βαασισμένο στην εργασία των Nakano-Kawano

a = nx.shortest_path(sp_gr, source=0)  # find all shortest paths
v = list(a.keys())[-1]     # select key for furthest node from source

[g1, s, t] = sp.bld(sp_gr, 0)    # Δημιουργία του series-parallel γράφου απο το δέντρο, s είναι το nest, t ειναι το food
G = nx.Graph()
G.add_nodes_from(g1.nodes)
nx.set_node_attributes(G, "node", name="kind")
G.nodes[t]["kind"] = "terminal"
G.nodes[s]["kind"] = "source"
print("G is connected: ", nx.is_connected(g1))
n = list(g1.nodes())[-1] + 1    # ευρεση μεγαλύτερου αναγνωριστικού κόμβου και αυξηση του κατα 1
for e in g1.edges:
    if e[2] != 0:   # ελεγχω αν η ακμή e έχει πολλαπλότητα διαφορετική του μηδενός
        G.add_node(n)
        G.nodes[n]["kind"] = "extra"
        G.add_edge(e[0], n)     # ενθέτω τον κόμβο n ώστε η ακμή e να αντικασταθεί απο 2
        G.add_edge(e[1], n)
        n += 1  # αυξανω το αναγνωριστικό του κόμβου
    else:
        G.add_edge(e[0], e[1])

pos = nx.nx_agraph.graphviz_layout(G, prog="dot", args="")
labels = nx.get_node_attributes(G, 'kind')
nx.draw(G, pos=pos, with_labels=True, labels=labels)
nx.draw(G, pos=pos, nodelist=[s], node_color="tab:red")
nx.draw(G, pos=pos, nodelist=[t], node_color="tab:green")
plt.show()
nx.write_graphml_lxml(G, "sp_graph_128e.graphml")

pos = nx.nx_agraph.graphviz_layout(sp_gr, prog="dot", args="")
labels = nx.get_node_attributes(sp_gr, 'type')
nx.draw(sp_gr, pos=pos, with_labels=True, labels=labels)
nx.draw(sp_gr, pos=pos, nodelist=[0], node_color="tab:red")
nx.draw(sp_gr, pos=pos, nodelist=[v], node_color="tab:green")
plt.show()


for i in sp_gr.nodes():
    sp_gr.nodes[i].pop("child", None)
    sp_gr.nodes[i].pop("parent", None)
sp_gr.nodes[0]["type"] = 's_root'
nx.write_graphml_lxml(sp_gr, "sp_tree_128e.graphml")
