import random
import sys
import time
import scipy
import math
import networkx
import numpy as np
from Base import graphIO
from itertools import combinations
import pandas as pd

prob_dict = {}

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
        nodes_of_interest_count = int(math.sqrt(len(graph.nodes))) * 5
    # for _ in range(NODES_OF_INTEREST_COUNT):
    #     observation_nodes.append(random.randint(0, len(graph.nodes) - 1))
    observation_nodes = random.sample(graph.nodes,nodes_of_interest_count)
    # print(f"Observation Set = {observation_nodes}")
    
    degrees = networkx.degree(graph)
    # print(degrees)
    degrees_dict = dict(degrees)

    
    for node in observation_nodes:
        degree_of_obs_node = degrees_dict[node]
        if degree_of_obs_node in prob_dict:
            prob_dict[degree_of_obs_node]+=1
        else:
            prob_dict[degree_of_obs_node]=1
        
    # degrees = [x[1] for x in degrees]
    # print(degrees_dict)
    # observed_degrees: List[int] = []
    # for node in observation_nodes:
    #     observed_degrees.append(degrees_dict[node])
    # ent = entropy(observed_degrees)
    # return ent


def betweenness_entropy(graph: networkx.Graph):
    betweennesses = networkx.betweenness_centrality(graph, normalized=False)
    betweennesses = list(dict(betweennesses).values())
    ent = entropy(betweennesses)
    return ent

def random_sample_entropy(graph,nodes_of_interest_count=0,iteration_count=0,centrality_func = random_degree_entropy):
    for _ in range(iteration_count):
        centrality_func(graph,nodes_of_interest_count)
    total = sum(prob_dict.values(), 0.0)
    a = {k: v / total for k, v in prob_dict.items()}
    # print("normalised: ",a)
    apna_ent=0
    for probability in a.values():
        apna_ent += probability * math.log2(probability)
    return apna_ent * -1

def laplacian_matrix(graph: networkx.Graph):
    # l=laplacian(graph)
    l = networkx.laplacian_matrix(graph).toarray()
    # laplacian log
    # print(l.shape,np.log(l).shape)
    # print(min(l))
    val = np.matmul(l,scipy.linalg.logm(l))
    # print(type(val[0][0]))
    trace_l = np.trace(val)
    return np.absolute(trace_l)


def test():
    #permutation stuff


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
    original_entropy = random_sample_entropy(networkx_graph,iteration_count=100)
    print(f"Original Entropy = {original_entropy:.2f}")
    proper_original_entropy = degreeEntropy(networkx_graph)
    print(f"Actual Entropy = {proper_original_entropy:.2f}")
    # for node in networkx_graph:
    #     copy = networkx_graph.copy()
    #     copy.remove_node(node)
    #     copy_entropy = degreeEntropy(copy)
    #     print(f"Node: {(node + 1):02}\tDegree: {networkx.degree(networkx_graph, node)} \tDelta H: {(original_entropy - copy_entropy):.3f}\tH after removal: {copy_entropy:.2f}")
    # print("Prob dict: ",prob_dict)
    
        

# test()
def testSubsetRandom(graph: networkx.Graph):
    degrees = networkx.degree(graph)
    degrees = list(map(lambda x: x[1], degrees))
    ent=0
    n=len(degrees)
    count=0
    for i in combinations(degrees,3):
        ent+=entropy(i)
        count+=1
    print("entropy: {0}, actual entropy: {1}".format(ent/count,degreeEntropy(graph)))


graph = graphIO()
graph.read_from_mtx_file(sys.argv[1])
# print(laplacian_matrix(graph.graph))

def Stats(graph: networkx.Graph, iteration: int):
    n = graph.number_of_nodes()
    sizes = [int(math.sqrt(n)), int(math.pow(n, .3333)), int(math.pow(n, .25)), n//100, 0]
    column_tags = ["sqrt","cube root","4th root","1%","standard"]
    stat_df = pd.DataFrame(columns = column_tags)
    for _ in range(iteration):
        lst = [random_sample_entropy(graph,sizes[i],30) for i in range(len(sizes))]
        #print(lst)
        # stat_df.append(dic,ignore_index=True)
        stat_df.loc[len(stat_df)] = lst
    stat_df.to_excel('trial.xlsx')
start = time.time()
Stats(graph.graph,1000)
end = time.time()
print(end-start)

        
            
        

