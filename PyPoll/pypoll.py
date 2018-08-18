#import the os module and csv module
import os
import csv

pypoll_csv = os.path.join('..', 'learnpython', 'election_data.csv')

#set lists to store data
candidate = []

#with open to read election_data.csv file
with open(pypoll_csv) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  reader=next(csvreader)

# Read each row of data after the header
  for row in csvreader:
      
#add candidate
    candidate.append(row[2])

# print election header

print("Election Results")
print("----------------------------")

# print total number of votes cast
print("Total Votes: " + str(len(candidate)))
print("----------------------------")

# print total for each candidate, wtih percentage and total votes
Khan = candidate.count("Khan")
khanpercent = int((Khan) / len(candidate) * 100)
print("Kahn: " + str(khanpercent) + "% (" + str(Khan) + ")")    

Correy = candidate.count("Correy")
correypercent = int((Correy) / len(candidate) * 100)
print("Corry: " + str(correypercent) + "% (" + str(Correy) + ")")

Li = candidate.count("Li")
Lipercent = int((Li) / len(candidate) * 100)
print("Li: " + str(Lipercent) + "% (" + str(Li) + ")")

OTooley = candidate.count("O'Tooley")
OTooleypercent = int((OTooley) / len(candidate) * 100)
print("O'Tooley " + str(OTooleypercent) + "% (" + str(OTooley) + ")")

print("----------------------------")


# write file