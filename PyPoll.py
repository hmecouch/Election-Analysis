

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of the candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

### Chaining files ###


#Add our dependencies

import csv

import os

#Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis","election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""

winning_count = 0

winning_percentage = 0

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:

        total_votes = total_votes + 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)
    
    for candidate_name in candidate_votes:

            votes = candidate_votes[candidate_name]

            vote_percentage = float(votes) / float(total_votes) * 100

            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)

            txt_file.write(candidate_results)


            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            if (votes > winning_count) and (vote_percentage > winning_percentage):


                winning_count = votes

                winning_percentage = vote_percentage

                winning_candidate = candidate_name

    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)

















