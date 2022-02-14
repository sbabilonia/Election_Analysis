#The data we need to retrieve
#1. The total number of votes
#2. List of candidates who recieved votes
#3. Percentage of votes each candidate recieved
#4. Total number of votes each candidate recieved
#5. The winner of the election based on popular vote
#Resources/election_results.csv
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
#Initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data, delimiter=',')

    # Read and print the header row.
    headers = next(file_reader)
    
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #mydict[key] will call a spec dict key or create one
            candidate_votes[candidate_name] = 0     #initializes each candidates votes to 0
        candidate_votes[candidate_name] += 1    #adds +1 vote to candidates total each time their name is read in a row

#save results to text file       
with open(file_to_save, "w") as txt_file:
    election_results = (
        f'\nElection Results \n'
        f'------------------- \n'
        f'Total Votes: {total_votes:,} \n'
        f'------------------- \n'
    )

    print(election_results, end = "")
    #save the final vote count to the text file
    txt_file.write(election_results)
        

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n'
        txt_file.write(candidate_results)
        #print(f'{candidate_name} received {vote_percentage:.1f}% of the vote.')

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count}\n'
        f'Winning Percentage: {winning_percentage:.1f}\n'
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)





# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)
# print(f'The time right now is {now}')

# #Assign a variable for the file to load and the path. Use if direct path is known
# file_to_load = 'Resources/election_results.csv'
# #Open the election results and read the file.
# #Syntax = file_variable = open(filename, mode)
# #modes: r - read, w = write, x = exclusive creation, a = append to existing file; creates or adds, + = read/write file
# election_data = open(file_to_load, 'r')
# #To do: perform analysis
# #Close the file
# election_data.close()


# #Import required modules
# import csv
# import os
# #Assign a variable for the file to load and the path. Use as an indirect path source
# file_to_load = os.path.join('Resources', 'election_results.csv') #join('folder','file')
# #format with the 'with' statement
# #with open(filename) as file_variable:
# with open(file_to_load) as election_data:
# #to do: perform election analysis
#     file_reader = csv.reader(election_data) # read file object with .reader fcn

#     for row in file_reader:
#         headers = next(file_reader)
#         print(headers)
    


# Create a filename variable to a direct or indirect path to the file. # variable name = open(filename,'mode').... variable_name.close()
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# # Create a filename variable to a direct or indirect path to the file. 
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file. #with open(filename,'mode') as variable_name
# with open(file_to_save, "w") as outfile:

#     # Write some data to the file.
#     outfile.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")    #\n = new line/return

