from networkx.algorithms.components.connected import is_connected
from networkx.classes.function import neighbors
from networkx.linalg.algebraicconnectivity import fiedler_vector
import scipy as sp
import networkx as nx
from scipy.io import mmread
from scipy.sparse.coo import coo_matrix
from scipy.sparse.linalg import eigs
from numpy import linalg as LA
import numpy as np
import csv

class Graph:
    def __init__(self, sparse):
        self.graph = nx.from_scipy_sparse_matrix(sparse)
        self.adj = nx.adjacency_matrix(self.graph)
        self.laplacian = nx.laplacian_matrix(self.graph)
    def degree_centrality(self):
        return nx.degree_centrality(self.graph)
    def closeness_centrality(self):
        return nx.closeness_centrality(self.graph)
    def betweenness_centrality(self):
        return nx.betweenness_centrality(self.graph, k = min(self.graph.number_of_nodes() , 500))
    def eigenvector_centrality(self):
        return nx.eigenvector_centrality(self.graph)
    def is_connected(self):
        return nx.is_connected(self.graph)
    def lfvc(self):
        if (not self.is_connected()):
            return "Not possible"
        fiedler_vector = nx.fiedler_vector(self.graph)
        lfvclist = []
        for i in self.graph.nodes(data = True):
            lfvcthis = 0
            for j in self.graph.neighbors(i[0]):
                lfvcthis += (fiedler_vector[j]-fiedler_vector[i[0]])*(fiedler_vector[j]-fiedler_vector[i[0]])
            lfvclist.append(lfvcthis)
        return lfvclist
    def neighbourhood_hopset(self, index, k = 10):
        nbrs = set([index])
        for l in range(k):
            nbrs = set((nbr for n in nbrs for nbr in self.graph[n]))
        return len(nbrs)
    def clustering_coefficient(self):
        return nx.clustering(self.graph)

karate = mmread('../assets/S_soc-karate.mtx')
internet = mmread('../assets/L_tech-internet-as.mtx')
# counter = 0
# rowindices = []
# colindices = []
# datacsv = []
# with open('../assets/M_web-edu.csv') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ' ', quotechar= '|')
#     next(csvreader)
#     for row in csvreader:
#         row = row[0].split(',')
#         rowindices.append(int(row[0]))
#         colindices.append(int(row[1]))
#         datacsv.append(int(row[3]))
#         counter += 1
# print(rowindices[1],colindices[1],datacsv[1], len(rowindices), len(colindices), len(datacsv), counter)
# print(counter)
# print(len(rowindices), len(colindices), len(datacsv))
# print([(counter//2, counter//2)])
# webedu = coo_matrix((datacsv, (rowindices, colindices)), (counter//2, counter//2))
webedu = mmread('../assets/M_web-edu.mtx')
print((webedu.shape[0]))
print(webedu.get_shape())

G = Graph(karate)
G1 = Graph(webedu)
G2 = Graph(internet)
print("graphs made")
c = G.is_connected()
c1 = G1.is_connected()
print(c)
print(c1)
# print(max(max(rowindices), max(colindices)), counter)
# print(G.lfvc())
# print(G1.lfvc())
# print(len(G.graph.nodes()))
# print("made adj matrix")
# dc = G.degree_centrality()
# cc = G.closeness_centrality()
# bc = G.betweenness_centrality()
# ec = G.eigenvector_centrality()
# print("lfvc")
# print(G.lfvc())
# print("Karate")
# print(dc,cc,bc,ec)
# # dc1 = G1.degree_centrality()
# # cc1 = G1.closeness_centrality()
# # bc1 = G1.betweenness_centrality()
# # ec1 = G1.eigenvector_centrality()
# # print("Web Edu")
# # print(dc1,cc1,bc1,ec1)
# dc2 = G2.degree_centrality()
# print("degree")
# print(G2.neighbourhood_hopset(0,2))
# # cc2 = G2.closeness_centrality()
# # print("closeness")
# bc2 = G2.betweenness_centrality()
# print("betweenness")
# ec2 = G2.eigenvector_centrality()
# print("Internet")
# print(dc2,bc2,ec2)
# nx.conductance(G,S:=(5,6))
# w,v = eigs(internet)
# print(w)
# print(v)