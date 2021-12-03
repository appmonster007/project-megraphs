import csv
import functools
import sys
 
o_file = sys.argv[1]
n_file = sys.argv[2]
with open(o_file,'r') as csvfile:
    with open(n_file,'w') as mtxfile:
        csvreader = csv.reader(csvfile)
        mtxfile.write("%%MatrixMarket matrix coordinate pattern symmetric \n")
        fields = next(csvreader)
        rows = []
        for row in csvreader:
            k = [int(x) for x in row[:2]]
            rows.append(k)
        max = functools.reduce(lambda a,b: [max(max(a),max(b)),min(min(a),min(b))], rows)
        mtxfile.write(""+str(max[0])+" "+str(max[0])+" "+str(len(rows))+"\n")
        rows = [[str(x) for x in r] for r in rows]
        k=""
        for i in range(len(rows)):
            rows[i].append("\n")
            k += " ".join(rows[i])
        mtxfile.writelines(k)
