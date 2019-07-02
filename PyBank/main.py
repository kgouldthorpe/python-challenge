#Get CSV
import csv
import os

#Bring in CSV
pybank_csv = os.path.join('Resources','budget_data.csv')

#Convert to library
budget_data = {}
#Read CSV
with open(pybank_csv, 'r') as csvfile:
  bankread = csv.reader(csvfile, delimiter=',')
  next(bankread)

  for row in bankread:
    budget_data[row[0]] = {"Profit/Losses":row[1]}
#Calculate number of months in the dataset
  month_count = len(budget_data)
  print(month_count)

#Calculate net total of Profit/Loss 
#net_total = 
    
#Calculate Average Change
    #average_chg = row[]
#Calculate greatest increse in profits
    
#Calculate greatest decrease in losses
#Set up Python Display
#Export data to Text File
    
    


  