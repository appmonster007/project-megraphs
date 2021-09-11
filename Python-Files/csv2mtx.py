import csv
file = "../assets/M_web-edu.csv"
n_file = "../assets/M_web-edu.mtx"
with open(file,'r') as csvfile:
    with open(n_file,'a') as mtxfile:
        csvreader = csv.reader(csvfile)
        mtxfile.write("%"+file+"\n")
        fields = next(csvreader)

        rows = []

        for row in csvreader:
            # rows.append(row)
            k = row[:2]
            k.append("\n")
            k = " ".join(k)
            rows.append(k)
        
        mtxfile.writelines(rows)

        print(fields)

        print(len(rows),len(row[0]))