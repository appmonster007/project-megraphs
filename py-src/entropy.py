import random
import sys
import math
import networkx
import numpy as np
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
# TODO: move sampling logic into this function
def random_degree_entropy(graph: networkx.Graph,nodes_of_interest_count = 0):
    
    observation_nodes = []
    if not nodes_of_interest_count:
        # nodes_of_interest_count =  len(graph.nodes) // 10
        nodes_of_interest_count = int(math.sqrt(len(graph.nodes))) * 10
    # for _ in range(NODES_OF_INTEREST_COUNT):
    #     observation_nodes.append(random.randint(0, len(graph.nodes) - 1))
    observation_nodes = random.sample(graph.nodes,nodes_of_interest_count)
    # print(f"Observation Set = {observation_nodes}")

    degrees = networkx.degree(graph)
    # print(degrees)
    degrees_dict = dict(degrees)
    # degrees = [x[1] for x in degrees]
    # print(degrees_dict)
    observed_degrees: List[int] = []
    for node in observation_nodes:
        observed_degrees.append(degrees_dict[node])
    ent = entropy(observed_degrees)
    return ent


def betweenness_entropy(graph: networkx.Graph):
    betweennesses = networkx.betweenness_centrality(graph, normalized=False)
    betweennesses = list(dict(betweennesses).values())
    ent = entropy(betweennesses)
    return ent

def random_sample_entropy(graph,nodes_of_interest_count=0,iteration_count=0,centrality_func = random_degree_entropy):
    ent_list=[]
    for _ in range(iteration_count):
        ent_list.append(np.array(centrality_func(graph,nodes_of_interest_count)))
    return sum(ent_list)/len(ent_list)
    

def test():
    graph = graphIO()
    graph.read_from_mtx_file(sys.argv[1])
    print(f"[INFO] file read complete")
    networkx_graph = graph.graph
    print(f"[INFO] extracted graph")

    # Select nodes to observe
    # observation_nodes = [];
    # NODES_OF_INTEREST_COUNT = len(networkx_graph.nodes) // 10
    # for _ in range(NODES_OF_INTEREST_COUNT):
    #     observation_nodes.append(random.randint(0, len(networkx_graph.nodes) - 1))
    # print(f"Observation Set = {observation_nodes}")

    # Store the original entropy as measured by random sample
    # original_entropy = random_degree_entropy(networkx_graph)
    original_entropy = random_sample_entropy(networkx_graph,iteration_count=10)
    print(f"Original Entropy = {original_entropy:.2f}")
    proper_original_entropy = degreeEntropy(networkx_graph)
    print(f"Actual Entropy = {proper_original_entropy:.2f}")
    for node in networkx_graph:
        copy = networkx_graph.copy()
        copy.remove_node(node)
        copy_entropy = random_sample_entropy(copy,iteration_count=50)
        print(f"Node: {(node + 1):02}\tDegree: {networkx.degree(networkx_graph, node)} \tDelta H: {(original_entropy - copy_entropy):.3f}\tH after removal: {copy_entropy:.2f}")
    
        

test()