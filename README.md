# Election_Analysis
module 3 Python

The objective of this module was to learn basic tools of Python in order to organize and visualize data collected for a Texas election. Tools utilized in this module included cloning github repos to local machines, pushing local files to github repo, with utilization of lists, dictionaries, methods, and functions. Skills taught in Python allows for the data collected in election_results.csv to be organized and visualized to display the results of the election. Inclusion of election_analysis.txt allows for the code output: total number of votes, total votes for each county, largest county turnout, and candidate statistics, including the winner of the election!
  
  Total number of votes cast during this election: Total Votes: 369,711
  
  total_votes = 0
  
  with open(file_to_load) as election_results:
    reader = csv.reader(election_results)
    
    header = next(reader)
    
    for row in reader:
      total_votes = total_votes += 1
      
  We initialize total_votes and set it to 0. This sets the vote count to 0
  
  As we loop through each row in election_results.csv we add to total votes + 1
  This is how we are able to collect the total number of votes in the election_results.csv
  
  for county_name in county_votes:
    county_vote_count = county_votes.get(county_name)
    county_vote_percentage = float(county_vote_count)/(float(total_votes)*100
    
  The above for loop allows us to collect the county vote count by referencing the each county in county_names within the county_votes dictionary
  each vote is added +1 per respective county:
  
  county_votes[county_name] = 0
  county_votes[county_name] += 1
  
  county vote percentage is calculated by dividing county vote count by the total number of votes cast * 100
  float is used to provide a provide %##.## format
  The largest county voter turnout was Denver with a vote count of 306055 (82.8%)
  
  Inside the for loop county_name in county_voter we insert a conditional if statement. If a county vote count was greater than any other vote count,
  we call it the largest county. This allows us to isolate the county with highest number of votes and set it equal to the largest county voter turnout.
  
    for county_name in county_voters:
       if county_vote_count > largest_count:
            largest_count = county_vote_count
            largest_county = county_name
    print(largest_county)
    
    
 Diana DeGette was the winner of this election with 272,892 (73.8%) votes
 
 for candidate_name in candidate_votes:
 ...
 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
 As we are looping through each candidate in candidate_votes dictionary, if the number of votes a candidate recieved was higher than any other candidate
 and if a candidates vote percentage were higher than the other candidates, then we set said candidate as the winning_candidate.
            
 This code has multiple applications in for data gathering following elections and can be applied as such:
 
  for president_elect in electoral_votes:
    if electoral_vote_count > largest_count:
    largest_count = electoral_vote_count
    largest_vote = presidential_elect
  print(largest_vote)
    
  another example may include adding a states electoral votes to a list:
   if state_name not in state_list:
            state_list.append(state_name)
  
  Applications such as the could be used to help extract the vote count from each state and determine a new president elect
