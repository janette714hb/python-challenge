#import the os module and csv module
import os
import csv

pypoll_csv = os.path.join("..", "pypoll", "election_data.csv")

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
print("Khan: " + str(khanpercent) + "% (" + str(Khan) + ")")

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

if khanpercent > .50:
	print("Winner: Khan")
elif correypercent > .50:
	print("Winner: Correy")
elif Lipercent > .50:
	print("Winner: Li")
else:
	print("Winner: O'Tooley")			

# write file
f = open("pypoll.txt","w")   #create add file in write mode
f.write("Khan: " + str(khanpercent) + "% (" + str(Khan) + ")")
f.write("Corry: " + str(correypercent) + "% (" + str(Correy) + ")")
f.write("Li: " + str(Lipercent) + "% (" + str(Li) + ")")
f.write("O'Tooley " + str(OTooleypercent) + "% (" + str(OTooley) + ")")
f.close()			#closing file object