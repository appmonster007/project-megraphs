import sys
import math
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

def test():
    graph = graphIO()
    graph.read_from_mtx_file(sys.argv[1])
    networkx_graph = graph.graph
    original_entropy = degreeEntropy(networkx_graph)
    print(f"Original Entropy = {original_entropy}")
    for node in networkx_graph:
        copy = networkx_graph.copy()
        copy.remove_node(node)
        copy_entropy = degreeEntropy(copy)
        print(f"Removing node {node} Resultant entropy: {copy_entropy}")
        print(f"Node {node} adds {original_entropy - copy_entropy} units of information")

        

test()