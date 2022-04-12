import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.io

import math
import time
import random


def poisson_noise():
    INTERVAL = .0005
    LAMBDA = 10.0
    events = {}

    def f(x, L):
      return 1 - math.exp(-L * x)


    start = time.time()

    while time.time() - start < 60:
      if random.random() < f(INTERVAL, LAMBDA):
        bucket = time.time() - start
        if bucket in events.keys():
            events[bucket] += 1
        else:
            events[bucket] = 1
      time.sleep(INTERVAL)

    print(events)
    return events

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
