import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.io

sizes = np.random.randint(100,300, 20)
p = []
for i in range(0, 20):
    t = []
    for j in range(0,20):
        if i == j:
            t.append(0.01)
        else:
            t.append(0.002)
    p.append(t)

g = nx.generators.stochastic_block_model(sizes, p, sparse = True)
nx.draw(g)
plt.show()
print(g)
gph = open("SBM.mtx", "xb")
scipy.io.mmwrite(gph, nx.linalg.graphmatrix.adjacency_matrix(g))
