from Base import GraphBase
import networkx as nx

# Sample proposed implementation for centrality
# To know more check out ./PROPSPEC.md
def degree_centrality(g: GraphBase):
    return nx.degree_centrality(g.graph)