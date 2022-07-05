import os
import csv

# Create a variable to hold data from the 'election_data.csv' file in the resources folder
PyPollcsv = os.path.join("Resources","election_data.csv")

# Create a list for number of votes, percentage of votes, and candidates
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open and read the csv file
with open(PyPollcsv, "r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csvreader)
    # Loop through the rows to get the count
    for row in csvreader:
        # Count the votes
        count = count + 1
        # Get the candidate names in column 3
        candidatelist.append(row[2])
        
    # Create a set from the candidatelist to get the unique candidate names
    for i in set(candidatelist):
        unique_candidate.append(i)
        # Find the total votes for each candidate
        y = candidatelist.count(i)
        vote_count.append(y)
        # Find the percentage of the vote for each candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winner_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winner_count)]
    
 
# Output results to the terminal first
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Output the same information to a txt file in the 'analysis' folder
election_results = os.path.join('analysis', 'election_results.txt')
with open(election_results, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
