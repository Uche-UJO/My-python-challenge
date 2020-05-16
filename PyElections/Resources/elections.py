# Import dependencies
import os, csv
from pathlib import Path 

# Assign file location with the pathlib library
#csv_file_path = Path('My-python-challenge', 'PyElections', 'houston_election_data.csv')

csv_file_path = Path('..', 'Resources', 'houston_election_data.csv')

import operator

# Declare Variables 
total_votes = 0

boykins_votes = 0
king_votes = 0
turner_votes = 0
buzbee_votes = 0
romero_votes = 0
smith_votes = 0
broze_votes = 0
#taylor_votes = 0
baker_votes = 0
houjami_votes = 0
vasquez_votes = 0
lovell_votes = 0


# Open csv in default read mode with context manager
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        #Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        #Count the number of times names appear and store in a list.
        #Use these values in percent vote calculation and in print statement.
        if row[0] == "Dwight A. Boykins": 
            boykins_votes +=1
        elif row[0] == "Bill King":
            king_votes +=1
        elif row[0] == "Sylvester Turner": 
            turner_votes +=1
        elif row[0] == "Tony Buzbee":
            buzbee_votes +=1
        elif row[0] == "Victoria Romero":
            romero_votes +=1
        elif row[0] == "Demetria Smith": 
            smith_votes +=1
        elif row[0] == "Derrick Broze":
            broze_votes +=1
        #elif row[0] == "Johnny J.T. Taylor":
            #taylor_votes +=1
        elif row[0] == "Kendall Baker": 
            baker_votes +=1
        elif row[0] == "Naoufal Houjami":
            houjami_votes +=1
        elif row[0] == "Roy J. Vasquez":
            vasquez_votes +=1
        elif row[0] == "Sue Lovell": 
            lovell_votes +=1

 # Create a dictionary out of the two lists above.
candidates = ["Dwight A. Boykins", "Bill King", "Sylvester Turner", "Tony Buzbee", "Victoria Romero", "Demetria Smith", "Derrick Broze", "Kendall Baker", "Naoufal Houjami", "Roy J. Vasquez", "Sue Lovell"]
votes = [boykins_votes, king_votes, turner_votes, buzbee_votes, romero_votes, smith_votes, broze_votes, baker_votes, houjami_votes, vasquez_votes, lovell_votes]

# Zip two lists together i.e. list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)


# Print a the summary of the analysis

boykins_percent = (boykins_votes/total_votes) *100
king_percent = (king_votes/total_votes) *100
turner_percent = (turner_votes/total_votes) *100
buzbee_percent = (buzbee_votes/total_votes) *100
romero_percent = (romero_votes/total_votes) *100
smith_percent = (smith_votes/total_votes) *100
broze_percent = (broze_votes/total_votes) *100
#taylor_percent = (taylor_votes/total_votes) *100
baker_percent = (baker_votes/total_votes) *100
houjami_percent = (houjami_votes/total_votes) *100
vasquez_percent = (vasquez_votes/total_votes) *100
lovell_percent = (lovell_votes/total_votes) *100


# Print the summary table
print(f"Houston Mayoral Election Results")
print(f"----------------------------")
print(f"Total Cast Votes: {total_votes}")
print(f"----------------------------")

print(f"Boykins: {boykins_percent:.3f}% ({boykins_votes})")
print(f"King: {king_percent:.3f}% ({king_votes})")
print(f"Turner: {turner_percent:.3f}% ({turner_votes})")
print(f"Buzbee: {buzbee_percent:.3f}% ({buzbee_votes})")
print(f"Romero: {romero_percent:.3f}% ({romero_votes})")
print(f"Smith: {smith_percent:.3f}% ({smith_votes})")
print(f"Broze: {broze_percent:.3f}% ({broze_votes})")
#print(f"Taylor: {taylor_percent:.3f}% ({taylor_votes})")
print(f"Baker: {baker_percent:.3f}% ({baker_votes})")
print(f"Houjami: {houjami_percent:.3f}% ({houjami_votes})")
print(f"Vasquez: {vasquez_percent:.3f}% ({vasquez_votes})")
print(f"Lovell: {lovell_percent:.3f}% ({lovell_votes})")

print(f"----------------------------")
print(f"Winner: {key}")
#print(f"1st Advancing Candidate: {key[0]}")
#print(f"2nd Advancing Candidate: {key[1]}")
print(f"----------------------------")



# Output file

output_file = Path('..', 'Resources', 'elections_summary.txt')

with open(output_file,"w") as file:

# Print Elections Summary to txt file
    file.write(f"Houston Mayoral Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Cast Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Boykins: {boykins_percent:.3f}% ({boykins_votes})")
    file.write("\n")
    file.write(f"King: {king_percent:.3f}% ({king_votes})")
    file.write("\n")
    file.write(f"Turner: {turner_percent:.3f}% ({turner_votes})")
    file.write("\n")
    file.write(f"Buzbee: {buzbee_percent:.3f}% ({buzbee_votes})")
    file.write("\n")
    file.write(f"Romero: {romero_percent:.3f}% ({romero_votes})")
    file.write("\n")
    file.write(f"Smith: {smith_percent:.3f}% ({smith_votes})")
    file.write("\n")
    file.write(f"Broze: {broze_percent:.3f}% ({broze_votes})")
    file.write("\n")
    #file.write(f"Taylor: {taylor_percent:.3f}% ({taylor_votes})")
    file.write(f"Baker: {baker_percent:.3f}% ({baker_votes})")
    file.write("\n")
    file.write(f"Houjami: {houjami_percent:.3f}% ({houjami_votes})")
    file.write("\n")
    file.write(f"Vasquez: {vasquez_percent:.3f}% ({vasquez_votes})")
    file.write("\n")
    file.write(f"Lovell: {lovell_percent:.3f}% ({lovell_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")