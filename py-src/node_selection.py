from collections import defaultdict
import random
import networkx as nx
from scipy.io import mmread
import sys
from typing import DefaultDict, Dict, Any, Set
import math

"""
Implementing algorithms for selecting nodes which are evenly dispersed throughout the graph
"""

def select(g: nx.Graph, selection_fraction: int):
    g = g.copy()
    selected: Set = set()
    rolling_distances: Dict[Any, int] = {}

    shortest_paths = {}
    seed = random.sample(list(g.nodes), 1)[0]
    # print(seed)
    
    for _ in range(int(len(g.nodes) * selection_fraction)):
        # Generate single source shortest paths
        shortest_paths[seed]: Dict[Any, list] = nx.single_source_shortest_path(g, seed)
        # print(f"shortest paths from node {shortest_paths[seed]}")

        # Find the farthest node(s) and its distance
        max_dist = max(len(path) for path in shortest_paths[seed].values())
        farthest_nodes = [s[-1] for s in shortest_paths[seed].values() if len(s) == max_dist]
        # print(f"largest distance from {seed} = {max_dist}")
        # print(f"farthest node from {seed} = {farthest_nodes}")

        for to_node in shortest_paths[seed].keys():
            if to_node in rolling_distances.keys():
                rolling_distances[to_node] += len(shortest_paths[seed][to_node])
            else: 
                rolling_distances[to_node] = len(shortest_paths[seed][to_node])

        # print(f"Rolling Distances = {rolling_distances}")

        old_seed = seed
        seed = max(
            [to_node for to_node in rolling_distances.keys()], 
            key= lambda node: rolling_distances[node]
        )
        possible_seed = [s for s in rolling_distances.keys() if rolling_distances[s] == rolling_distances[seed]]
        # print(f"possible seeds = {possible_seed}")
        seed = random.sample(possible_seed, 1)[0]
        # print(f"Updated seed to {seed}")
        selected.add(old_seed)
        g.remove_node(old_seed)

    return selected, shortest_paths

def sampled_betweenness_centrality(g: nx.Graph, selection_fraction: int):
    selected, shortest_paths = select(g, selection_fraction)
    betweenness: Dict[Any, int] = {}

    for start_node in shortest_paths.keys():
        for end_node in shortest_paths[start_node].keys():
            
            if start_node == end_node: continue

            path = shortest_paths[start_node][end_node]
            for node in path: 
                if node in betweenness.keys():
                    betweenness[node] += 1 / (len(selected) * len(g.nodes))
                else:
                    betweenness[node] = 1 / (len(selected) * len(g.nodes))
    
    return betweenness

def test():
    print(f"reading {sys.argv[1]}")
    graph = nx.from_scipy_sparse_matrix(mmread(sys.argv[1]))
    size_of_graph = len(graph.nodes)
    # chosen_nodes, _ = select(graph, 0.2)
    # print(chosen_nodes)

    sb = sampled_betweenness_centrality(graph,  1/math.sqrt(size_of_graph))
    print(sb[15] / sb[0])

    b = nx.betweenness_centrality(graph, int(math.sqrt(size_of_graph)))
    print(b[15] / b[0])
    # nx.draw(graph, with_labels=True)

test()