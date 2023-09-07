import csv 
with open('industry.csv',newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ',quotechar='|')
    for row in data :
        #print(' '.join(row))
        print(row)
type(data)
#type(row)