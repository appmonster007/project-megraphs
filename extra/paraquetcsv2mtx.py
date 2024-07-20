import pandas as pd

fld = "assets/reddit_threads/"

df = pd.read_csv("assets/converted.csv")

df.sort_values(by='num_nodes', inplace=True, ascending=False)
df.sort_values(by='y', inplace=True, ascending=False)

for idx, row in df[:200].iterrows():
    with open(f"{fld}{idx}.mtx", 'w') as file:
        file.write("%%MatrixMarket matrix coordinate pattern symmetric \n")
        nodes = int(row['num_nodes'])
        edges = eval(row['edge_index'])
        file.write(f"{nodes} {nodes} {len(edges[0])} \n")
        for i in range(len(edges[0])):
            file.write(f"{edges[0][i]} {edges[1][i]} \n")


