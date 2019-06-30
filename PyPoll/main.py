#Get CSV
import csv
import os
from collections import defaultdict

pypoll_csv = os.path.join('Resources', 'election_data.csv')

with open(pypoll_csv, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)
  
  for row in csvreader:
    
    #calcuate total votes cast
    total_votes = len(list(csvreader))
    print(total_votes)

    #calculate complete list of candidates

    #calculate total vote per candidate

    #calculate percentages of votes for each candidate

    #calculate winner of the election
#Read CSV
