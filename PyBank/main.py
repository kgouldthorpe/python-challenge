#Get CSV
import csv
import os
import numpy as np
pybank_csv = os.path.join('Resources', 'budget_data.csv')

#Read CSV
with open(pybank_csv, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)

#Calculate number of months in the dataset
  month_count = len(list(csvreader))
  print(month_count)

#Read CSV again
with open(pybank_csv, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)
  net_total = 0

#Convert row 1 to np 
  for row in csvreader:
    np_row = np.array(list(row[1]))
    
#Calculate net total of Profit/Loss   
    net_total = sum(np_row)
    print(net_total)
    


  