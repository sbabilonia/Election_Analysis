#dependencies
import os
import csv

#Assign variable to load file path
file_to_load = os.path.join('Resources', 'election_results.csv')

#Assign variable to save the file path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#initilize counter
total_votes = 0

#create empty list and dict
candidate_options = []
candidate_votes = {}

#open election results and read the file
with open(file_to_save) as election_data:
    file_reader = csv.reader(election_data)

    #Read header row and discard from results
    headers = next(file_reader)

    #print each row in csv file
    for row in file_reader:
        #add to the total vote count ****
        total_votes += 1

        #print candidate name for each row
        candidate_name = row[2]

        #if candidates name is not already on the candidates list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #sets each candidates vote to zero. allows for initial vote tallying
            candidate_votes[candidate_name] = 0
print(candidate_votes)