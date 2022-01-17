from Base import Graph
import pandas as pd
import csv
import sys
#visualization libraries, not required as such for main algorithm
import networkx as nx

filename = sys.argv[1]
filename = 'M_web-edu.mtx'
filename = 'S_soc-karate.mtx'
G2 = Graph(mtxfilepath=f'../assets/{filename}')

N = 50
nodes_count = G2.graph.number_of_nodes()
k_val = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 
    (nodes_count**(1/2))/nodes_count, 
    (nodes_count**(1/3))/nodes_count, 
    (nodes_count**(1/4))/nodes_count]
k_val = sorted(k_val)

g_noi = G2.nodes_of_interest()
print(f'{filename}', nodes_count, G2.graph.number_of_edges(), G2.is_connected())


for x in k_val:
    csv_file = open(f'{x}_{filename}', 'w')
    writer = csv.writer(csv_file)

    bc_vals = dict()

    bc = nx.betweenness_centrality(G2.graph, k = int(nodes_count*x))
    for i in bc:
            bc_vals[i] = [bc[i]]
    for _ in range(N-1):
        bc = nx.betweenness_centrality(G2.graph, k = int(nodes_count*x))
        for i in bc:
            bc_vals[i].append(bc[i])

    for k, v in bc_vals.items():
        l = [k]
        l.extend(v)
        writer.writerow(l)



# print(type(bc))