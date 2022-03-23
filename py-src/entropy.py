from locale import normalize
import sys
import math
from turtle import clear
from matplotlib.pyplot import grid
import networkx
from Base import graphIO

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

def test():
    graph = graphIO()
    graph.read_from_mtx_file(sys.argv[1])
    print(f"[INFO] file read complete")
    networkx_graph = graph.graph
    print(f"[INFO] extracted graph")
    original_entropy = betweenness_entropy(networkx_graph)
    print(f"Original Entropy = {original_entropy:.2f}")

    
    for node in networkx_graph:
        copy = networkx_graph.copy()
        copy.remove_node(node)
        copy_entropy = betweenness_entropy(copy)
        print(f"Node: {(node + 1):02}\tDegree: {networkx.degree(networkx_graph, node)} \tDelta H: {(original_entropy - copy_entropy):.2f}\tH after removal: {copy_entropy:.2f}")
    
        

test()