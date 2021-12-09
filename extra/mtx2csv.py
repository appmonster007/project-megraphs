from scipy import sparse
from scipy.io import mmread
import numpy as np
import csv
import sys

mat = mmread(sys.argv[1]+'.mtx').astype(int).toarray()
mat_array = mat.tolist()

with open(sys.argv[1]+'.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)    
    csvwriter.writerow('Source,Target,Type,weight'.split(','))
    for i in range(len(mat_array)):
        for j in range(i,len(mat_array)):
            if(mat_array[i][j]==1):
                csvwriter.writerow([str(i+1), str(j+1), 'Undirected', str(1)])