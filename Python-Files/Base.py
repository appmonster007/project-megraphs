from matplotlib import pyplot as plt
import networkx as nx
from scipy.io import mmread
from scipy.sparse.coo import coo_matrix
# from os import stat
# from networkx.algorithms.components.connected import is_connected
# from networkx.classes.function import neighbors
# from networkx.linalg.algebraicconnectivity import fiedler_vector
# import scipy as sp
import networkx as nx
from scipy.io import mmread
from scipy.sparse.coo import coo_matrix
from scipy.sparse.linalg import eigs
# from numpy import linalg as LA
import numpy as np
import statistics


class graphIO:
    """
    Base for all graph related activity in the program.
    Exposes functionality required by all graph(like) objects in the program.
    """
    def __init__(self):
        self.graph: nx.Graph = None

    
    def read_from_mtx_file(self, filepath: str):
        """
        Allows users to read graph data from mtx files.
        the mtx file represents the graph in adjacency matrix form.
        """
        print(f"[INFO] attempting to read from {filepath}")
        spmat: coo_matrix = mmread(filepath)
        print(f"[INFO] read to sparse matrix")
        self.graph = nx.from_scipy_sparse_matrix(spmat)
        print(f"[INFO] constructed networkx graph")

    def draw_to_png(self, outpath: str, label: str = None):
        """
        Draws the graph to png image
        """
        assert outpath[-4:] == ".png", f"[ERROR] unexpected output file format recieved {outpath[-4:]} expected .png"
        if (self.graph):
            # generate the graph layout
            # Easier to log stuff this way
            print('[INFO] attempting to generate nodes/edges layout')
            pos = nx.kamada_kawai_layout(self.graph)
            print('[INFO] nodes/Edges layout generated')
            if label:
                print(f"[INFO] using key {label} to label nodes")
                labelset = nx.get_node_attributes(self.graph, label)
                nx.draw(self.graph, pos, labels=labelset)
            else:
                nx.draw(self.graph, pos)
            plt.savefig(outpath)
        else:
            print("[WARN] cannot draw undefined graph to image")
            print("[INFO] read something into graph before drawing")

class Graph:
    """
    Encapsulating a graph as a single object
    Graph Class encapsulates a networkx graph and exposes medthods for finding centtralities and related metrics
    Currently implemented metrics include:
    - Degree Centrality
    - Closeness Centrality
    - Betweenness Centrality
    - Eigenvector Centrality
    - LFVC
    """
    
    def __init__(self, **kwargs):
        if('sparse' in kwargs):
            self.graph = nx.from_scipy_sparse_matrix(kwargs['sparse'])
        elif('mtxfilepath' in kwargs):
            self.graph = nx.from_scipy_sparse_matrix(mmread(kwargs['mtxfilepath']))
        else:
            raise ValueError("Provide sparse matrix or mtx file path")
            
        self.adj = nx.adjacency_matrix(self.graph)
        self.laplacian = nx.laplacian_matrix(self.graph)

    # @property
    # def __graph
    def __setGraph(self, filepath: str):
        # self.graph = nx.from_scipy_sparse_matrix(mmread(filepath))
        return mmread(filepath)

    def draw_to_png(self, outpath: str, label: str = None):
        """
        Draws the graph to png image
        """
        assert outpath[-4:] == ".png", f"[ERROR] unexpected output file format recieved {outpath[-4:]} expected .png"
        if (self.graph):
            # generate the graph layout
            # Easier to log stuff this way
            print('[INFO] attempting to generate nodes/edges layout')
            pos = nx.kamada_kawai_layout(self.graph)
            print('[INFO] nodes/Edges layout generated')
            if label:
                print(f"[INFO] using key {label} to label nodes")
                labelset = nx.get_node_attributes(self.graph, label)
                nx.draw(self.graph, pos, labels=labelset)
            else:
                nx.draw(self.graph, pos)
            plt.savefig(outpath)
        else:
            print("[WARN] cannot draw undefined graph to image")
            print("[INFO] read something into graph before drawing")

    
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


    def eigenvector_centrality_node(self, node):
        eigenvector , eigen_val = self.eigenvector_atindex(-1)
        nodes = list(self.graph.nodes(data = True))
        n = nodes[node]
        inv = 1/eigen_val
        centrality = 0
        for i in self.graph.neighbors(n[0]):
            data = self.graph.get_edge_data(i, n[0], 0)
            centrality += data["weight"] * eigenvector[i]
        return centrality * inv


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
        fiedler_vector = self.eigenvector_atindex(1)[0]
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


    def ego_centrality_node(self, node):
        g = nx.ego_graph(self.graph, node)
        nodes = list(g.nodes(data = True))
        n = node
        for i in nodes:
            if i[0] == node:
                n = i
                break
        centrality =  nx.betweenness_centrality(g)
        return centrality[node]


    def nodes_of_interest(self):
        l = list(nx.degree_centrality(self.graph))
        mean = statistics.mean(l)
        median = statistics.median_high(l)
        closest_mean = min(l, key = lambda x:abs(x-mean))
        max_value = max(l)
        min_value = min(l)
        return l.index(median), l.index(closest_mean), l.index(min_value), l.index(max_value)


    def eigenvector_atindex(self, a):
        eig_values, eig_vectors = eigs(self.adj)
        evr = np.sort(eig_values.real)
        vector_pos = np.where(eig_values.real == evr[a])[0][0]
        vector = np.transpose(eig_vectors)[vector_pos]
        eig_val = evr[a]
        return vector.real, eig_val
