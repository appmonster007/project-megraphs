from matplotlib import pyplot as plt
import networkx as nx
from networkx.algorithms import tree
from networkx.classes.function import subgraph
from numpy.core.fromnumeric import argmax
from scipy.io import mmread
from scipy.sparse.coo import coo_matrix
from scipy.sparse.linalg import eigs
import numpy as np
from copy import deepcopy 
import statistics

# from os import stat
# from networkx.algorithms.components.connected import is_connected
# from networkx.classes.function import neighbors
# from networkx.linalg.algebraicconnectivity import fiedler_vector
# import scipy as sp
# from numpy import linalg as LA


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
        if('nx_graph' in kwargs):
            self.graph: nx.Graph = kwargs['nx_graph']
        elif('sparse' in kwargs):
            self.graph: nx.Graph = nx.from_scipy_sparse_matrix(kwargs['sparse'])
        elif('mtxfilepath' in kwargs):
            self.graph: nx.Graph = nx.from_scipy_sparse_matrix(mmread(kwargs['mtxfilepath']))
        else:
            raise ValueError("Provide sparse matrix or mtx file path")
            
        self.adj = nx.adjacency_matrix(self.graph)
        self.laplacian = nx.laplacian_matrix(self.graph)

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
        eigenvector , eigen_val = self.eigenvector_atindex(self.adj, -1)
        # nodes = list(self.graph.nodes(data = True))
        # n = nodes[node]
        eig_dict = dict()
        j = 0
        for x in self.graph.nodes:
            eig_dict[x] = eigenvector[j]
            j+=1

        inv = 1/eigen_val
        centrality = 0
        for i in self.graph.neighbors(node):
            data = self.graph.get_edge_data(i, node, 0)
            centrality += data["weight"] * eig_dict[i]
        return centrality * inv


    def is_connected(self):
        return nx.is_connected(self.graph)


    def lfvc(self):
        if (not self.is_connected()):
            return []

        # fiedler_vector = nx.fiedler_vector(self.graph)
        # lfvclist = []
        # for i in self.graph.nodes(data = True):
        #     lfvcthis = 0
        #     for j in self.graph.neighbors(i[0]):
        #         lfvcthis += (fiedler_vector[j]-fiedler_vector[i[0]])*(fiedler_vector[j]-fiedler_vector[i[0]])
        #     lfvclist.append(lfvcthis)
        # return lfvclist

        fv = self.eigenvector_atindex(self.laplacian, 1)[0]
        # fv = nx.fiedler_vector(self.graph)
        LFVC_arr = [sum([(fv[j]-fv[i[0]])**2 for j in self.graph.neighbors(i[0])]) for i in self.graph.nodes(data = True)]
        return LFVC_arr
        

    def lfvc_node(self, node):
        if (not self.is_connected()):
            return 0

        # nodes = list(self.graph.nodes(data = True))
        # n = nodes[node]

        # lfvcthis = 0
        # fiedler_vector = self.eigenvector_atindex(self.adj, 1)[0]
        # fiedler = fiedler_vector[n[0]]
        # for j in self.graph.neighbors(n[0]):
        #     lfvcthis += (fiedler_vector[j]-fiedler)*(fiedler_vector[j]-fiedler)
        # return lfvcthis
            
        fv = self.eigenvector_atindex(self.laplacian, 1)[0]
        fv_dict = dict()
        i = 0
        for x in self.graph.nodes:
            fv_dict[x] = fv[i]
            i+=1

        lfvc = sum([(fv_dict[j]-fv_dict[node])**2 for j in self.graph.neighbors(node)])
        return lfvc
        

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


    def eigenvector_atindex(self, graph, a):
        eig_values, eig_vectors = eigs(graph)
        evr = np.sort(eig_values.real)
        vector_pos = np.where(eig_values.real == evr[a])[0][0]
        vector = np.transpose(eig_vectors)[vector_pos]
        eig_val = evr[a]
        return vector.real, eig_val


    def greedy_community_detection(self, **kwargs):

        def _node_lfvc(lcc_sg):
            # corresponding fiedler vector
            Y = self.eigenvector_atindex(nx.laplacian_matrix(lcc_sg), 1)[0]

            # finding argmax 
            k,p = {},0
            for x in lcc_sg.nodes(data=True):
                k[x[0]] = Y[p]
                p+=1

            LFVC_dict = {sum([(k[j]-k[i[0]])**2 for j in lcc_sg.neighbors(i[0])]) : i[0] for i in lcc_sg.nodes(data = True)}
            m = max(LFVC_dict.keys())
            i_star = LFVC_dict[m]
            return i_star

        # TODO: add greedy function for other centralities with lcc subgraph as parameter and returns (i*) node

        def getLCCSubgraph(G):
            nodes = max(nx.connected_components(G), key=len)
            subgraph = nx.subgraph(G, list(nodes))
            return subgraph

        q = kwargs['q']
        R = set()
        G = deepcopy(self.graph)
        for _ in range(q):
            # finding largest connected component
            lcc_sg : nx.Graph = getLCCSubgraph(G)

            if(kwargs['function']=='node_lfvc'):
                i_star = _node_lfvc(lcc_sg)

            R.add(i_star)
            G.remove_node(i_star)
        
        # Vs_cap = set()
        # for x in R:
        #     j = self.graph.neighbors(x)
        #     Vs_cap = Vs_cap.union(j)
        # Vs_cap = Vs_cap.union(R)
        # return Vs_cap

        nu, om = set(), set()
        cc_found = False
        for cc in nx.connected_components(G):
            vs_cap = list(set(cc))
            nu, om = set(), set()
            for x in R: 
                found = [self.graph.has_edge(x,i) for i in vs_cap]
                if(any(found)):
                    om.add(x) # blue nodes
            nu = om.union(vs_cap)
            if (len(R) == len(om)):
                cc_found = True
                break
        
        if(not cc_found):
            scc = sorted(nx.connected_components(G), key=len, reverse=True)
            for cc in scc:
                vs_cap = list(set(cc))
                nu, om = set(), set()
                for x in R: 
                    found = [self.graph.has_edge(x,i) for i in vs_cap]
                    if(any(found)):
                        om.add(x) # blue nodes
                nu = om.union(vs_cap)
                if(len(om) > 0):
                    break

        return (om, nu)