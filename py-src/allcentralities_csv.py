from Base import Graph
import pandas as pd
import csv
import sys
#visualization libraries, not required as such for main algorithm
import networkx as nx


if len(sys.argv) == 1:
    filename = 'M_web-edu.mtx'
else:
    filename = sys.argv[1]
G1 = Graph(mtxfilepath=f'../assets/{filename}')

dc1 = G1.degree_centrality()
ec1 = G1.eigenvector_centrality()
egc1 = G1.ego_centrality()
clc1 = G1.clustering_coefficient()
nhc1 = G1.neighbourhood_hopset_graph(2)
bc1 = G1.betweenness_centrality()
lfvc_val = G1.lfvc()
csv_file = open(f'{filename}_csv', 'w')
writer = csv.writer(csv_file)
len = G1.graph.number_of_nodes()
print(len)
for i in range(0, len):
    row = []
    row.append(i)
    row.append(dc1[i])
    row.append(ec1[i])
    row.append(lfvc_val[i])
    row.append(clc1[i])
    row.append(egc1[i])
    row.append(nhc1[i])
    #betweenness is commented out for now
    #row.append(bc1[i])
    writer.writerow(row)
# print(type(bc))