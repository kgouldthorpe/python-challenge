#Get CSV
import csv
import os

pypoll_csv = os.path.join('Resources', 'election_data.csv')

#set up data as dictionary
election_data = {}

with open(pypoll_csv, 'r') as csvfile:
  pypollfile = csv.reader(csvfile, delimiter=',')
  next(pypollfile)

  for row in pypollfile:
    election_data[row[0]] = {'County':row[1], 'Candidate': row[2]}

#Total_votes
  total_votes = len(election_data)
  print(total_votes)  

#Find unique candidates
  for candidate in election_data:
    print(candidate) 


#Set up Python Display
print("Election Results")
print("----------------------------------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------------------------------")
print("Average Change: " + "$" + str(avg_change))
print("Greatest Increase in Profits: " + "$" + str(increase))
print("Greatest Decrease in Profits: " + "$" + str(decrease))
Print("-----------------------------------------------------")

#Export data to Text File
with open('Results.txt', "w") as txt_file:  
  txt_file.write("Financial Anaylsis" + "\n")
  txt_file.write("Total Months: " + str(month_count) + "\n")  
  txt_file.write("Total: $" + str(net_total) + "\n")    
  txt_file.write("Average Change: $" + str(avg_change) + "\n")
  txt_file.write("Greatest Increase in Profits: $" + str(increase) + "\n")
  txt_file.write("Greatest Decrease in Profits: $" + str(decrease) + "\n")