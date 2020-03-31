## Create list for counties

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Counties
counties = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

         # Add to the total vote count.
        total_votes += 1

        # Print the county name from each row.
        county_name = row[1]

        #If the candidate does not match any existing candidate...
        if county_name not in counties:
            #Add it to the list of counties.
            counties.append(county_name)

# Print the counties list.
print(counties)

#Counties list
counties=["Jefferson","Denver","Arapahoe"]

##Create county dictionary 

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
counties = []
#Declare the empty dictionary.
county_votes={}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
         # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        county_name = row[1]

        #If the candidate does not match any existing candidate...
        if county_name not in counties:
            #Add it to the list of candidates.
            counties.append(county_name)

            #Begin tracking that candidate's vote count.
            county_votes[county_name]=0

        #Add a vote to that candidate's count.
        county_votes[county_name] +=1

# Print the county vote dictionary.
print(county_votes)

#county dictionary (key,value; county, county_votes)
county_votes={"Jefferson":38855,"Denver":306055, "Arapahoe": 24801}

##Percentage of County Votes

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
counties = []
#Declare the empty dictionary.
county_votes={}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
         # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        county_name = row[1]

        #If the candidate does not match any existing candidate...
        if county_name not in counties:
            #Add it to the list of candidates.
            counties.append(county_name)

            #Begin tracking that candidate's vote count.
            county_votes[county_name]=0

        #Add a vote to that candidate's count.
        county_votes[county_name] +=1

# Percentage of votes for each county
# Iterate through the county list.
for county in county_votes:
    # Retrieve vote count of a county.
    votes = county_votes[county]
    # Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100
    # Print the county name and percentage of votes.
    print(f"{county}: received {vote_percentage:.1f}% of the vote.") 