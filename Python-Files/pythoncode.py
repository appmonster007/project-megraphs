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
        return nx.betweenness_centrality(self.graph)
    def eigenvector_centrality(self):
        return nx.eigenvector_centrality(self.graph)
karate = mmread('soc-karate.mtx')
internet = mmread('tech-internet-as.mtx')
counter = 0
rowindices = []
colindices = []
datacsv = []
with open('Medium-web-edu.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ' ', quotechar= '|')
    next(csvreader)
    for row in csvreader:
        row = row[0].split(',')
        rowindices.append(int(row[0]))
        colindices.append(int(row[1]))
        datacsv.append(int(row[3]))
        counter += 1
print(counter)
print(len(rowindices), len(colindices), len(datacsv))
print([(counter//2, counter//2)])
webedu = coo_matrix((datacsv, (rowindices, colindices)), (counter//2, counter//2))
print((webedu.shape[0]))
print(webedu.get_shape())

G = Graph(karate)
G1 = Graph(webedu)
G2 = Graph(internet)
#uncomment below to read internet graph instead
# G=nx.from_scipy_sparse_matrix(internet)
print("graphs made")
print(G.adj, G1.adj, G2.adj)
print(G.laplacian, G1.laplacian, G2.laplacian)
print("made adj matrix")
dc = G.degree_centrality()
cc = G.closeness_centrality()
bc = G.betweenness_centrality()
ec = G.eigenvector_centrality()
print("Karate")
print(dc,cc,bc,ec)
dc1 = G1.degree_centrality()
cc1 = G1.closeness_centrality()
bc1 = G1.betweenness_centrality()
ec1 = G1.eigenvector_centrality()
print("Web Edu")
print(dc1,cc1,bc1,ec1)
dc2 = G2.degree_centrality()
cc2 = G2.closeness_centrality()
bc2 = G2.betweenness_centrality()
ec2 = G2.eigenvector_centrality()
print("Internet")
print(dc2,cc2,bc2,ec2)
nx.conductance(G,S:=(5,6))
w,v = eigs(internet)
print(w)
print(v)