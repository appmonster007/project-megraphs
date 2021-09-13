from os import stat
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
import statistics

class Graph:
    def __init__(self, sparse):
        self.graph = nx.from_scipy_sparse_matrix(sparse)
        self.adj = nx.adjacency_matrix(self.graph)
        self.laplacian = nx.laplacian_matrix(self.graph)
    def degree_centrality(self):
        return nx.degree_centrality(self.graph)
    def closeness_centrality(self):
        return nx.closeness_centrality(self.graph)
    def closeness_centrality_node(self, node):
        return nx.closeness_centrality(self.graph, node)
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
    def lfvc_node(self, node):
        if (not self.is_connected()):
            return "Not possible"
        lfvcthis = 0
        nodes = list(self.graph.nodes(data = True))
        n = nodes[node]
        fiedler_vector = nx.fiedler_vector(self.graph)
        fiedler = fiedler_vector[n[0]]
        for j in self.graph.neighbors(n[0]):
            lfvcthis += (fiedler_vector[j]-fiedler)*(fiedler_vector[j]-fiedler)
        return lfvcthis
    def neighbourhood_hopset(self, index, k = 10):
        nbrs = set([index])
        for l in range(k):
            nbrs = set((nbr for n in nbrs for nbr in self.graph[n]))
        return len(nbrs)
    def clustering_coefficient(self):
        return nx.clustering(self.graph)
    def clustering_coefficient_node(self, node):
        return nx.clustering(self.graph, node)
    #def ego_centrality()
    def nodes_of_interest(self):
        l = list(nx.degree_centrality(self.graph))
        mean = statistics.mean(l)
        median = statistics.median_high(l)
        closest_mean = min(l, key = lambda x:abs(x-mean))
        max_value = max(l)
        min_value = min(l)
        return l.index(median), l.index(closest_mean), l.index(min_value), l.index(max_value)

karate = mmread('soc-karate.mtx')
internet = mmread('tech-internet-as.mtx')
counter = 0
rowindices = []
colindices = []
datacsv = []
webedu = mmread('web-edu.mtx')
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
print(G.lfvc_node(0))
print(G1.lfvc_node(0))
print(len(G.graph.nodes()))
print("made adj matrix")
print(G1.nodes_of_interest())
print(G.nodes_of_interest())
print(G2.nodes_of_interest())
print("Nodes of interest")
dc = G.degree_centrality()
cc = G.closeness_centrality()
bc = G.betweenness_centrality()
ec = G.eigenvector_centrality()
clc = G.clustering_coefficient_node(0)
print("lfvc")
print(G.lfvc())
print("Karate")
print(dc,cc,bc,ec)
print("Clusters of node 1")
print(clc)
dc1 = G1.degree_centrality()
cc1 = G1.closeness_centrality_node(0)
bc1 = G1.betweenness_centrality()
ec1 = G1.eigenvector_centrality()
print("Web Edu")
print(dc1,cc1,bc1,ec1)
dc2 = G2.degree_centrality()
print("degree")
print(G2.neighbourhood_hopset(0,2))
# cc2 = G2.closeness_centrality()
# print("closeness")
bc2 = G2.betweenness_centrality()
print("betweenness")
ec2 = G2.eigenvector_centrality()
print("Internet")
print(dc2,bc2,ec2)
nx.conductance(G,S:=(5,6))
w,v = eigs(internet)
print(w)
print(v)