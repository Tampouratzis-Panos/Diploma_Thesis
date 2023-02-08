import networkx as nx
import numpy
""" Creates Series Parallel Graph based on the paper of Kawano-Nakano Generating All Series Parallel Graphs"""


def a0(graph, ri, sp):
    """implements the function of a0-s and a0-p depending on value of sp"""
    n = graph.number_of_nodes()  # πλήθος ακμών του γράφου δέντρο για τους series-parallel
    graph.add_node(n, type='n', child=[])  # προσθέτω κόμβο φύλλο normal
    graph.add_edge(ri, n)   # προσθέτω ακμή απο τον κόμβο πατέρα στο νέο παιδί
    graph.nodes[ri]['child'].append(n)  # ενθέτω το νέο παιδι στην λίστα παιδιων του κόμβου πατέρα
    graph.nodes[n]['parent'] = ri   # θέτω τιμή για πατέρα στο νέο κόμβο
    n += 1   # αυξάνω το πλήθος τον κόμβων κατα 1
    graph.add_node(n, type='n', child=[])   # προσθέτω το δεύτερο παιδί στον κόβμο πατέρα
    graph.add_edge(ri, n)   # προσθέτω ακμή απο τον κόμβο πατέρα στο νέο παιδί
    graph.nodes[ri]['child'].append(n)  # ενθέτω το νέο παιδι στην λίστα παιδιων του κόμβου πατέρα
    graph.nodes[n]['parent'] = ri   # θέτω τιμή για πατέρα στο νέο κόμβο

    graph.nodes[ri]['type'] = sp    # Θέτω τιμή τύπου κόμβου πατέρα #### εκανες αλλαγη εδω ηταν με διπλή if

    return graph, n-1   # επιστρέφω τον γράφο και το αναγνωριστικο του τελευταίου αφαιρέσιμου κόμβου


def a1(graph, ri):
    """implements the function of a1, add single node to graph"""
    n = graph.number_of_nodes()             # πλήθος ακμών του γράφου δέντρο για τους series-parallel
    graph.add_node(n, type='n', child=[])   # προσθέτω κόμβο φύλλο normal
    graph.add_edge(ri, n)                   # προσθέτω ακμή απο τον κόμβο πατέρα στο νέο παιδί
    graph.nodes[ri]['child'].append(n)      # ενθέτω το νέο παιδι στην λίστα παιδιων του κόμβου πατέρα
    graph.nodes[n]['parent'] = ri           # θέτω τιμή για πατέρα στο νέο κόμβο

    return graph, n                         # επιστρέφω τον γράφο και το αναγνωριστικο του τελευταίου αφαιρέσιμου κόμβου


def subgraph_nodes(v, sp):
    """ Create list of subtree nodes for graph sp"""
    sb_nodes = []   # λιστα κόμβων υπογράφου
    for vx in sp.nodes[v]['child']:     # Διατρέχω λίστα παιδιων κόμβου v
        temp = subgraph_nodes(vx, sp)   # καλω αναδραμικά μεχρι να φτασω σε κόμβο v χωρίς παιδια
        sb_nodes.extend(temp)           # καλω την extend ωστε να προσθέσω την λιστα temp
    sb_nodes.append(v)                  # προσθέτω τον καλούντα κομβο τους κόμβου του υπογράφου

    return sb_nodes


def sp_generator(m, t):
    """creates series parallel tree graph"""
    # m is the number of edges of series-parallel graph
    # t is string specifying type of root node for the tree
    sp_gr = nx.Graph()  # το δεντρο για τον series-parallel γραφο

    n = 0   # αρχικοποιώ το πλήθος των κόμβων που δρά και σαν το αναγνωριστικό τον κόμβων
    sp_gr.add_node(n, type='n', child=[], parent="None")    # προσθέτω τον κόμβο ρίζα
    [sp_gr, lr] = a0(sp_gr, n, t)   # προσθέτω δυο παιδία ωστε να ξεκινησει η διαδικασία και θέτω τον τύπο της ρίζα όπως μου την έχεδι δώσει ο χρήστης στην μεταβλητη t
    m -= 2  # αφαιρω δύο ακμες απο το σύνολο που ακμών που πρεπει να έχει ο τελικος series-parallel γράφος
    while m != 0:   # όσο υπάρχουν ακομα ακμές να προστεθούν
        rp = nx.shortest_path(sp_gr, source=0, target=lr)  # βρίσκω το μονοπάτι προς τον τελευταίο αφαιρέσιμο κόμβο (last removable)
        i = numpy.random.randint(0, rp.__len__())   # επιλέγω τυχαία κόμβο στο μονοπάτι, Επιλέγω απο του ακεραιους στο διάστημα [0, μήκος μονοπατιού)
        # να το κάνω ώστε όταν επιλέγεται ο τελευταίος  κομβος να κανει αυτόματα το a3 που πρέπει.
        p = numpy.random.randint(1, 4)  # Επιλέγω τυχαία ποια απο τις δυνατές δράσεις πρόσθεσης κόμβου θα επιλέξω
        if p == 1:
            # a1
            if sp_gr.nodes[rp[i]]['type'] != 'n':   # αν ο επιλεγμένος κόμβο δεν ειναι τύπου normal
                [sp_gr, lr] = a1(sp_gr, rp[i])  # προσθέτω κομβο φύλλο στον επιλεγμένο κόμβο
                m -= 1  # μειώνω το πλήθος ακμών που μένει να προστεθούν
        elif p == 2:
            # a2
            if sp_gr.nodes[rp[i]]['child'].__len__() == 2 and m-1 >= 0:  # αν ο επιλεγμενος κομβος έχει δύο παιδιά # ( χρειάζεται το m-1????)
                w = sp_gr.nodes[rp[i]]['child'][1]  # Επιλέγω το δεξιότερο
                if sp_gr.nodes[w]['type'] == 'n':   # αν ειναι φύλλο, δηλαδη τύπου normal
                    m -= 1  # μειώνω το πλήθος ακμών που μένει να προστεθούν
                    anc = sp_gr.nodes[w]['parent']  # κραταω την τιμή του επιλεγμένου κόμβου και ελεγχω τον τύπο του και αλλάζω το δεξιότερο παιδί στον αλλό τύπο κόμβου απο τον πατέρα
                    if sp_gr.nodes[anc]['type'] == 's':
                        [sp_gr, lr] = a0(sp_gr, w, 'p')
                    else:
                        [sp_gr, lr] = a0(sp_gr, w, 's')
        elif p == 3:
            # a3
            if lr == rp[i] and m-1 >= 0:    # ελεγχω αν ο επιλεγμένος κόμβος ειναι ο τελευταίος αφαιρέσιμος
                m -= 1
                anc = sp_gr.nodes[rp[i]]['parent']  # κραταω την τιμή του επιλεγμένου κόμβου και ελεγχω τον τύπο του και αλλάζω τον τύπο του τελευταίου αφαιρέσιμου κόμβου στον αλλό τύπο κόμβου απο τον πατέρα

                if sp_gr.nodes[anc]['type'] == 's':
                    [sp_gr, lr] = a0(sp_gr, rp[i], 'p')
                else:
                    [sp_gr, lr] = a0(sp_gr, rp[i], 's')

    return sp_gr, lr


def bld(sp_gr, src):
    """adds edges to series parallel graph based on the sp tree"""
    o = nx.MultiGraph()     # γράφος εξόδου
    sp = nx.shortest_path(sp_gr, source=src) # find all shortest paths
    v = list(sp.keys())[-1]     # select key for furthest node from source
    pv = sp_gr.nodes[v]['parent']   # select parent of furthest node from source

    s = 0   # nest
    t = 1   # food
    o.add_node(s)   # προσθέτω των κόμβο nest στον γράφο εξόδου
    o.add_node(t)   # προσθέτω των κόμβο food στον γράφο εξόδου
    o.add_edge(s, t)    # προσθέτω ακμή αναμεσα στου κόμβους

    while pv in sp_gr.nodes and pv != "None":
        if sp_gr.nodes[pv]['type'] == 'p':  # ελεγχω αν ο πατέρας υποδηλώνει πάραλληλη σχέση αναμεσα στις ακμές
            for cv in sp_gr.nodes[pv]['child']:     # διατρέχω όλους τους κόμβους παιδία
                if sp_gr.nodes[cv]['type'] == 'n' and cv != v:  # αν ο κόμβος ειναι normal και δεν είναι ο κομβος απο τον οποιο ήρθα / ο βαθύτερος στην πρώτη εκτέλεση
                    o.add_edge(s, t)    # προσθέτω ακμή αναμεσα στους κομβους nest και food
                elif cv != v:   # στην περιπτωση που ο κομβος δεν έιναι normal και δεν είναι ο κομβος απο τον οποιο ήρθα / ο βαθύτερος στην πρώτη εκτέλεση
                    # υπάρχει υπογράφος που πρέπει να διατρέξω απο τον βαθύτερο κόμβο προς την ρίζα
                    sb_nodes = subgraph_nodes(cv, sp_gr)    # ο κομβος cv δεν είναι normal αρα έχει παιδια, βρίσκω τους κόμβους στον υπογράφο με ρίζα τον κόμβο cv
                    g = sp_gr.subgraph(sb_nodes)    # αποσπώ τον υπογράφο από το δέντρο series-parallel sp_gr
                    [o1, s1, t1] = bld(g, cv)   # εκτελώ την διαδικασία και επιστρέφω τον γράφο
                    # αλλαζω ετικέτες στους κόμβους του γράφου ώστε να μήν χάσω του κόμβους s και  t κατα την ένωση του γράφου o και o1
                    i = 0   # μεταβλητη μετρητης
                    mapping = {}    # λεξικο που απαιτείται απο την συνάρτηση αλλαγής ετικετών
                    for vx_o in o.nodes():  # διατρέχω όλλους τους κόμβους του γράφου o
                        mapping[vx_o] = i   # προσθέτω ώς κλειδι την ετικέτα του κόμβου στον γραφο ο και ως τιμη την καινουργια ετικέτα
                        if s == vx_o:   # αλλαζω τις τιμές που έχω κρατήσει για κομβο nest
                            s = i
                        elif t == vx_o:     # αλλαζω τις τιμές που έχω κρατήσει για κομβο food
                            t = i
                        i += 1
                    o = nx.relabel_nodes(o, mapping=mapping)    # αλλαζω ετικέτες στον γραφο o
                    n = o.number_of_nodes()     # βρισκω το πληθος των κόμβων
                    # υποθέτω s1 = 0
                    s1 = s1 + n     # μετατοπιζω τo s1 κατα πλήθος κόμβων του γράφου ο
                    t1 = t1 + n     # μετατοπιζω τo t1 κατα πλήθος κόμβων του γράφου ο
                    o = nx.disjoint_union(o, o1)
                    for e in o.edges(s1):       # για όλες τις ακμές του s1
                        o.add_edge(e[1], s)     # προσθέτω ακμή αναμεσα στον αλλό κόμβο και το s
                    o.remove_node(s1)           # αφαιρω τον κομβο s1 απο τον τελικό γράφο ώστε να εχω ένα s
                    for e in o.edges(t1):       # για όλες τις ακμές του t1
                        o.add_edge(e[1], t)     # προσθέτω ακμή αναμεσα στον αλλό κόμβο και το t
                    o.remove_node(t1)           # αφαιρω τον κομβο t1 απο τον τελικό γράφο ώστε να εχω ένα t
                    o = nx.convert_node_labels_to_integers(o, first_label=0)    # αλλαζω τις ετικέτες ωστε να πηγαίνουν απο 0 εως πληθος κόμβων μειον ενα
        elif sp_gr.nodes[pv]['type'] == 's':  # ελεγχω αν ο πατέρας υποδηλώνει σειριακη σχέση αναμεσα στις ακμές
            for cv in sp_gr.nodes[pv]['child']:     # διατρέχω όλους τους κόμβους παιδία
                if sp_gr.nodes[cv]['type'] == 'n' and cv != v:  # αν ο κόμβος ειναι normal και δεν είναι ο κομβος απο τον οποιο ήρθα / ο βαθύτερος στην πρώτη εκτέλεση
                    # Οι κομβοι ειναι αριθμημένοι απο το 0 έως πλήθος κόμβων μειον ενα.
                    n = o.number_of_nodes()  # αναγνωριστικό νέου κόμβου
                    o.add_node(n)       # προσθέτω τον κόμβο
                    o.add_edge(t, n)    # προσθέτω ακμή αναμεσα στο κόμβο food και τον νέο κόμβο
                    t = n   # αλλαζω τον κόμβο food
                elif cv != v:   # στην περιπτωση που ο κομβος δεν έιναι normal και δεν είναι ο κομβος απο τον οποιο ήρθα / ο βαθύτερος στην πρώτη εκτέλεση
                    # υπάρχει υπογράφος που πρέπει να διατρέξω απο τον βαθύτερο κόμβο προς την ρίζα
                    sb_nodes = subgraph_nodes(cv, sp_gr)    # ο κομβος cv δεν είναι normal αρα έχει παιδια, βρίσκω τους κόμβους στον υπογράφο με ρίζα τον κόμβο cv
                    g = sp_gr.subgraph(sb_nodes)    # αποσπώ τον υπογράφο από το δέντρο series-parallel sp_gr
                    [o1, s1, t1] = bld(g, cv)   # εκτελώ την διαδικασία και επιστρέφω τον γράφο
                    n = o.number_of_nodes()     # βρισκω το πληθος των κόμβων
                    # υποθέτω s1 = 0
                    s1 = s1 + n     # μετατοπιζω τo s1 κατα πλήθος κόμβων του γράφου ο
                    t1 = t1 + n     # μετατοπιζω τo t1 κατα πλήθος κόμβων του γράφου ο
                    o = nx.disjoint_union(o, o1)
                    for e in o.edges(s1):       # διατρέχω όλες τις ακμές του s1
                        o.add_edge(e[1], t)     # προσθέτω ακμές αναμεσα στους κόμβους του γραφου ο1 που συνδέονταν με τον κομβο s1 και του κόμβου t του γράφου o
                    o.remove_node(s1)
                    t = t1
                    # αλλαζω ετικέτες στους κόμβους του γράφου ώστε να μήν χάσω του κόμβους s και  t κατα την ένωση του γράφου o και o1
                    i = 0   # μεταβλητη μετρητης
                    mapping = {}    # λεξικο που απαιτείται απο την συνάρτηση αλλαγής ετικετών
                    for vx_o in o.nodes():  # διατρέχω όλλους τους κόμβους του γράφου o
                        mapping[vx_o] = i   # προσθέτω ώς κλειδι την ετικέτα του κόμβου στον γραφο ο και ως τιμη την καινουργια ετικέτα
                        if s == vx_o:   # αλλαζω τις τιμές που έχω κρατήσει για κομβο nest
                            s = i
                        elif t == vx_o:     # αλλαζω τις τιμές που έχω κρατήσει για κομβο food
                            t = i
                        i += 1
                    o = nx.relabel_nodes(o, mapping=mapping)    # αλλαζω ετικέτες στον γραφο o
        v = pv  # κάνω τρέχων κόμβο τον πατέρα
        pv = sp_gr.nodes[v]['parent']  # επιλέγω τον πατέρα του νέου τρέχοντος κόμβου και πηγαίων στην επόμενη επανάληψη
        # όταν ο τρέχων κόμβος είναι η ρίζα του δέντρου sp_gr ο πατέρας είναι "None" και τερματίζει ο βρόγχος



    return o, s, t
