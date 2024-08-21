from Base import Graph
import pandas as pd
import csv
import time
import sys
#visualization libraries, not required as such for main algorithm
import networkx as nx


if len(sys.argv) == 1:
    filename = 'L_tech-internet-as.mtx'
else:
    filename = sys.argv[1]
G1 = Graph(mtxfilepath=f'../assets/{filename}')

# dc1 = G1.degree_centrality()
# ec1 = G1.eigenvector_centrality()
# egc1 = G1.ego_centrality()
# clc1 = G1.clustering_coefficient()
# nhc1 = G1.neighbourhood_hopset_graph(2)


# lfvc_val = G1.lfvc()
csv_file = open(f'{filename}_csv', 'w')
writer = csv.writer(csv_file)
len = G1.graph.number_of_nodes()
print(len)

import os

csv_file = open('data_csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['Nodes','Normal Betweenness','Custom Betweenness','Degree', 'Closeness'])

reddit_file_director = '../assets/reddit_threads'
directory = os.fsencode(reddit_file_director)
    
for file in os.listdir(directory):
    print(directory.decode('UTF-8') + '/' + file.decode('UTF-8'))
    G1 = Graph(mtxfilepath=directory.decode('UTF-8') + '/' + file.decode('UTF-8'))
    start = time.thread_time_ns()
    bc1 = nx.betweenness_centrality(G1.graph)
    print(f"\t\tNumber of edges:{G1.graph.number_of_edges()} and nodes:{G1.graph.number_of_nodes()}")
    normal_b = (time.thread_time_ns() - start)
    print(f"\t\tTime normal algorithm: {normal_b:.4F} nano seconds")
    start = time.thread_time_ns()
    rbc1 = G1.betweenness_centrality()
    random_b = (time.thread_time_ns() - start)
    print(f"\t\tTime custom algorithm: {random_b:.4F} nano seconds")
    start = time.thread_time_ns()
    dbc1 = G1.degree_centrality()
    degree = (time.thread_time_ns() - start)
    print(f"\t\tTime degree algorithm: {degree:.4F} nano seconds")
    start = time.thread_time_ns()
    cc1 = G1.closeness_centrality()
    closess = (time.thread_time_ns() - start)
    print(f"\t\tTime closeness algorithm: {closess:.4F} nano seconds")
    writer.writerow([G1.graph.number_of_nodes(),normal_b,random_b,degree, closess])


reddit_file_director = '../assets/proteins'
directory = os.fsencode(reddit_file_director)
    
for file in os.listdir(directory):
    print(directory.decode('UTF-8') + '/' + file.decode('UTF-8'))
    G1 = Graph(mtxfilepath=directory.decode('UTF-8') + '/' + file.decode('UTF-8'))
    start = time.thread_time_ns()
    bc1 = nx.betweenness_centrality(G1.graph)
    print(f"\t\tNumber of edges:{G1.graph.number_of_edges()} and nodes:{G1.graph.number_of_nodes()}")
    normal_b = (time.thread_time_ns() - start)
    print(f"\t\tTime normal algorithm: {normal_b:.4F} nano seconds")
    start = time.thread_time_ns()
    rbc1 = G1.betweenness_centrality()
    random_b = (time.thread_time_ns() - start)
    print(f"\t\tTime custom algorithm: {random_b:.4F} nano seconds")
    start = time.thread_time_ns()
    dbc1 = G1.degree_centrality()
    degree = (time.thread_time_ns() - start)
    print(f"\t\tTime degree algorithm: {degree:.4F} nano seconds")
    start = time.thread_time_ns()
    cc1 = G1.closeness_centrality()
    closess = (time.thread_time_ns() - start)
    print(f"\t\tTime closeness algorithm: {closess:.4F} nano seconds")
    writer.writerow([G1.graph.number_of_nodes(),normal_b,random_b,degree, closess])
