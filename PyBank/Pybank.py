#import the os module and csv module
import os
import csv

pybank_csv = os.path.join("..", "pybank", "budget_data.csv")

#set lists to store data
revenue = []
date = []

data = {}

#with open to read budget_data.csv file
with open(pybank_csv) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  reader=next(csvreader)

# Read each row of data after the header
  for row in csvreader:
      
    #add dates and values to dict
    data[row[0]] = int(row[1])

# Total months is total entries of data set
print("Total Months: " + str(len(data.keys())))

# Total net amount of "Profit/Losses" over the entire period is the sum of the values
print("Total: $" + str(sum(data.values())))

# sum(data.values()) / len(data.keys())

print("Average Change: $" + str(sum(data.values()) / len(data.keys())))

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = sorted(data.values(), reverse=True)[0]
greatest_increase_key = sorted(data, key=data.get, reverse=True)[0]
print("Greatest Increase in Profits: " + greatest_increase_key + " ($" + str(greatest_increase) + ")")

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = sorted(data.values(), reverse=False)[0]
greatest_decrease_key = sorted(data, key=data.get, reverse=False)[0]
print("Greatest Decrease in Profits: " + greatest_decrease_key + " ($" + str(greatest_decrease) + ")")

# write file
f = open("pybank.txt","w")   #create add file in write mode
f.write("Total: $" + str(sum(data.values())))
f.write("Average Change: $" + str(sum(data.values()) / len(data.keys())))
f.write("Greatest Increase in Profits: " + greatest_increase_key + " ($" + str(greatest_increase) + ")")
f.write("Greatest Decrease in Profits: " + greatest_decrease_key + " ($" + str(greatest_decrease) + ")")
f.close() #close file