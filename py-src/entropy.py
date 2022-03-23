import random
import sys
import math
import networkx
from Base import graphIO

from typing import List

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

# Let us assume the entropy only considers few nodes
def random_degree_entropy(graph: networkx.Graph, observation_nodes: List[int]):
    degrees = networkx.degree(graph)
    degrees = list(map(lambda x: x[1], degrees))
    observed: List[int] = []
    for node in observation_nodes:
        observed.append(degrees[node])
    ent = entropy(observed)
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

    # Select nodes to observe
    observation_nodes = [];
    NODES_OF_INTEREST_COUNT = 20;
    for _ in range(NODES_OF_INTEREST_COUNT):
        observation_nodes.append(random.randint(0, len(networkx_graph.nodes)))
    print(f"Observation Set = {observation_nodes}")

    # Store the original entropy as measured by random sample
    original_entropy = random_degree_entropy(networkx_graph, observation_nodes)
    print(f"Original Entropy = {original_entropy:.2f}")
    

    
    for node in networkx_graph:
        copy = networkx_graph.copy()
        copy.remove_node(node)
        copy_entropy = random_degree_entropy(copy, observation_nodes)
        print(f"Node: {(node + 1):02}\tDegree: {networkx.degree(networkx_graph, node)} \tDelta H: {(original_entropy - copy_entropy):.2f}\tH after removal: {copy_entropy:.2f}")
    
        

test()