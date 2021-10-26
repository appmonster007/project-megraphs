from Base import GraphBase
import networkx as nx

def fluidsim(graph: GraphBase, iters=100):
    for node in graph.graph:
        if graph.graph.degree[node] < 2:
            graph.graph.nodes[node]['pressure'] = 1.0
        else:
            graph.graph.nodes[node]['pressure'] = 0.0

    for _ in range(iters):
        for node in graph.graph:
            for neighbour in graph.graph.neighbors(node):
                deltaP = graph.graph.nodes[node]['pressure'] - graph.graph.nodes[neighbour]['pressure']
                graph.graph.nodes[node]['pressure'] -= deltaP * 0.01
                graph.graph.nodes[neighbour]['pressure'] += deltaP * 0.01
    