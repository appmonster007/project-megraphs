from collections import defaultdict
import random
import networkx as nx
from scipy.io import mmread
import sys
from typing import DefaultDict, Dict, Any, Set

"""
Implementing algorithms for selecting nodes which are evenly dispersed throughout the graph
"""

def select(g: nx.Graph, selection_fraction: int):
    g = g.copy()
    selected: Set = set()
    rolling_distances: Dict[Any, int] = {}

    shortest_paths = {}
    seed = random.sample(list(g.nodes), 1)[0]
    print(seed)
    
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
        # print(f"Updated seed to {seed}")
        selected.add(old_seed)
        g.remove_node(old_seed)

    return selected

def test():
    print(f"reading {sys.argv[1]}")
    graph = nx.from_scipy_sparse_matrix(mmread(sys.argv[1]))
    chosen_nodes = select(graph, 0.2)
    print(chosen_nodes)

    sum_shortest_paths = 0
    count = 0
    for node in chosen_nodes:
        for other in chosen_nodes:
            if node != other:
                sum_shortest_paths += nx.shortest_path_length(graph, node, other)
                count += 1

    print(f"Average shortest path = {sum_shortest_paths / count}")
    print(f"diameter of graph = {nx.diameter(graph)}")

    # nx.draw(graph, with_labels=True)

test()