import csv 
data = csv.DictReader(open("industry.csv"))
print("CSV file as a dictionary:\n")
for row in data:
    print(row)