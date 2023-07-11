import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
pos = nx.nx_agraph.graphviz_layout(G, prog='dot', args='-Grankdir=TB')
# pos=nx.nx_pydot.graphviz_layout(G, prog='dot', args='-Grankdir=TB')
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
