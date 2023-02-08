import networkx as nx
import matplotlib.pyplot as plt
import random as r
import sp_func as sp


name = "sp_tree_"
name1 = "sp_graph_"
end = ".graphml"
fname = ""
edges = 34

j = 0
m = 0
while j < 10:
    off = r.randint(0, 5)
    print(m, off)
    m = edges + off
    [sp_gr, lr] = sp.sp_generator(m, 's')    # δημιουργία δεντρου ακμών series-parallel γραφου βαασισμένο στην εργασία των Nakano-Kawano
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
    pos = nx.nx_agraph.graphviz_layout(sp_gr, prog="dot", args="")
    labels = nx.get_node_attributes(sp_gr, 'type')
    nx.draw(sp_gr, pos=pos, with_labels=True, labels=labels)
    nx.draw(sp_gr, pos=pos, nodelist=[0], node_color="tab:red")
    plt.show()

    for i in sp_gr.nodes():
        sp_gr.nodes[i].pop("child", None)
        sp_gr.nodes[i].pop("parent", None)
    sp_gr.nodes[0]["type"] = 's_root'

    ans = input("Do you want to save? [y/n] ")
    if ans == "y":
        fname = name+str(j)+end
        nx.write_graphml(sp_gr, fname)
        fname = name1+str(j)+end
        nx.write_graphml(G, fname)
        print("Graphs Saved")
        j += 1
