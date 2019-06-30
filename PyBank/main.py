#Get CSV
import csv
import os

#Bring in CSV
pybank_csv = os.path.join('Resources','budget_data.csv')

#Read CSV
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

#Calculate number of months in the dataset
 for row in csvreader:
    month_count = len(list(row[0]))
    print(month_count)

#Calculate net total of Profit/Loss 
#net_total = 
    
#Calculate Average Change
    #average_chg = row[]
#Calculate greatest increse in profits
    
#Calculate greatest decrease in losses
#Set up Python Display
#Export data to Text File
    
    


  