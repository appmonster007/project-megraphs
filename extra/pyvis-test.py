import networkx as nx
from scipy.io import mmread
import numpy as np
import matplotlib.pyplot as plt
from pyvis.network import Network
import graphistry as gp
mmgraph = mmread('assets/web-edu.mtx')
# mmgraph = mmread('assets/S_soc-karate.mtx')
G = nx.from_scipy_sparse_matrix(mmgraph)
# nx.draw(G)
# plt.show()

# nt = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
# # nt = Network(height='750px', width='100%')
# nt.add_nodes([i for i in range(G.number_of_nodes())])
# for n1,n2 in G.edges:
#     nt.add_edge(int(n1),int(n2))
# # print(nt)
# nt.repulsion(node_distance=150, spring_length=400)
# nt.show_buttons(filter_=True)
# nt.show('webedu_nt.html')

# print(G.is_directed())
gp.register(api=3, protocol="https", server="hub.graphistry.com", username="<?>", password="<?>") 
gp.bind(source='src', destination='dst', node='nodeid').plot(G)
# print(type(gp.graph(G)))
