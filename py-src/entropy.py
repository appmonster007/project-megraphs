from locale import normalize
import sys
import math
from turtle import clear
from matplotlib.pyplot import grid
import networkx
from Base import graphIO
import copy

def entropy(sample: list):
    distribution = {}
    for element in sample:
        if (element in distribution.keys()):
            distribution[element] = distribution[element] + 1
        else:
            distribution[element] = 1
    ent = 0.0
    total_samples = len(sample)
    for element in distribution.keys():
        probability = distribution[element] / total_samples
        ent += probability * math.log2(probability)
    return -ent

def degreeEntropy(graph: networkx.Graph):
    degrees = networkx.degree(graph)
    degrees = list(map(lambda x: x[1], degrees))
    ent = entropy(degrees)
    return ent

def betweenness_entropy(graph: networkx.Graph):
    betweennesses = networkx.betweenness_centrality(graph, normalized=False)
    betweennesses = list(dict(betweennesses).values())
    ent = entropy(betweennesses)
    return ent;

# def Diff_of_entropy(graph: networkx.Graph):
#     original_graph = copy.deepcopy(graph)
#     original_entropy = betweenness_entropy(original_graph)
#     for u in graph.copy():
#         graph.remove_node(u)
#         copy_entropy = betweenness_entropy(graph)
#         if(copy_entropy < original_entropy):
#             # remove that node from original grp
#             original_graph.remove_node(u)
#             # recalculate original grps entropy
#             original_entropy = betweenness_entropy(original_graph)
#         else:
#             graph = original_graph.copy()
#     return original_graph, original_entropy

def test():
    graph = graphIO()
    graph.read_from_mtx_file(sys.argv[1])
    print(f"[INFO] file read complete")
    networkx_graph = graph.graph
    print(f"[INFO] extracted graph")
    original_entropy = betweenness_entropy(networkx_graph)
    print(f"Original Entropy = {original_entropy:.2f}")

    # print("no of nodes before " + str(networkx_graph.number_of_nodes()))
    # a, b = Diff_of_entropy(networkx_graph)
    # print("no of nodes after " + str(a.number_of_nodes()))
    # print(b)
    for node in networkx_graph:
        copy = networkx_graph.copy()
        copy.remove_node(node)
        copy_entropy = betweenness_entropy(copy)
        print(f"Node: {(node + 1):02}\tDegree: {networkx.degree(networkx_graph, node)} \tDelta H: {(original_entropy - copy_entropy):.2f}\tH after removal: {copy_entropy:.2f}")
    
        

test()