from matplotlib import pyplot as plt
import networkx as nx
from scipy.io import mmread
from scipy.sparse.coo import coo_matrix


class GraphBase:
    """
    Base for all graph related activity in the program.
    Exposes functionality required by all graph(like) objects in the program.
    """
    def __init__(self):
        self.graph: nx.Graph = None

    
    def read_from_mtx_file(self, filepath: str):
        """
        Allows users to read graph data from mtx files.
        the mtx file represents the graph in adjacency matrix form.
        """
        spmat: coo_matrix = mmread(filepath)
        self.graph = nx.from_scipy_sparse_matrix(spmat)

    def draw_to_png(self, outpath: str):
        """
        Draws the graph to png image
        """
        assert outpath[-4:] == ".png", f"[ERROR] unexpected output file format recieved {outpath[-4:]} expected .png"
        if (self.graph):
            pos = nx.kamada_kawai_layout(self.graph)
            nx.draw(self.graph, pos)
            plt.savefig(outpath)
        else:
            print("[WARN] cannot draw undefined graph to image")
            print("[INFO] read something into graph before drawing")