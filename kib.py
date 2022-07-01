#!/usr/bin/env python3
import csv 
import numpy as np
from collections import Counter
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-i", "--inputfile", required=True,
   help="first operand")

args = ap.parse_args()

# Calculate the sum
#print("Sum is {}".format(int(args['foperand'])))
print('Input file is: ',args.inputfile)
file = open(args.inputfile)

type(file)

csvreader = csv.reader(file)

rows = []
product_name= []
quantity= []
Brand= []
uniq_pr_name= []
unique_quantity= []
uniq_brand= []
uniq_num_ordr= []
dummy=[]
most_pop= []
### Read the Input file and do some analysis
for row in csvreader:
    product_name.append(row[2])
    quantity.append(row[3])
    Brand.append(row[4])
    rows.append(row)
uniq_pr_name= np.unique(product_name)
uniq_brand= np.unique(Brand)
file.close()

### create 0_input_example.csv
###Analysis Process
for upr in uniq_pr_name:
    total_quantity = 0
    for row in rows:
        if upr == row[2]:
            total_quantity = int(total_quantity) + int(row[3])
    unique_quantity.append(total_quantity/len(rows))

###Write Process
with open('0_input_example.csv', 'w', newline='') as file_0:
    writer = csv.writer(file_0)
    for i in range(len(uniq_pr_name)):
        writer.writerow([uniq_pr_name[i], unique_quantity[i]])


### create 1_input_example.csv
###Analysis Process
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

for upr in uniq_pr_name:
    dummy= []
    for row in rows:
        if upr == row[2]:
            dummy.append(row[4])
    most_pop.append(most_frequent(dummy))

###Write Process
with open('1_input_example.csv', 'w', newline='') as file_1:
    writer = csv.writer(file_1)
    for i in range(len(uniq_pr_name)):
        writer.writerow([uniq_pr_name[i], most_pop[i]])



