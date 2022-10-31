# Election_Analysis

## Project Overview
Use data given to me about a recent congressional election to perform an audit and give the results to an election employee.

1. Calculate the total number of votes cast.
2. Get a list of the counties invovled in the voting.
3. Calculate the total number of votes cast in each county.
4. Breakdown each county's percentage of the total votes.
5. Get a complete list of candidates who received votes.
6. Calculate the total number of votes each candidate reveived.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election base on popular vote.

## Resources
-Data Source: election_results.csv
-Software: Python 3.10.8, Visual Code Studio, 1.72.2

## Election-Audit Results
The analysis of the election show that:
-There were 369,711 votes cast in the election.
-The counties voting in the election:
  -Jefferson
  -Denver
  -Arapahoe
-The total votes in each county and percentage of the total were:
  -Jefferson county had 38,855 votes cast and 10.5% of the total election votes
  -Denver county had 306,055 votes cast and 82.8% of the total election votes
  -Arapahoe county had 24,801 votes cast and 6.7% of the total election votes
-Result:
  -Denver county had the largest amount of voters in this election.
-The candidates were:
  -Charles Casper Stockham
  -Diana DeGette
  -Raymon Anthony Doane

-The results were:
  -Charles Casper Stockham received 23% of the vote and 85,213 votes
  -Diana Degette received 73.8% of the vote and 272,892 votes
  -Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
 -The winner of the election was:
  -Diana Degette, who received 73.8% of the vote and 272,892 votes.
  
  ## Election-Audit Summary
  The script used to audit this election can easily be used to do the same with other future elections by making a few small changes to the code. After downloading the data from a new election the first change would be to change the path to the csv file holding the data. <img width="429" alt="Election-Audit-path" src="https://user-images.githubusercontent.com/114922260/199110899-12dab8d0-983b-43bf-bd30-31e97849d35b.png"> Looking at this picture you can see the part of the script that would need changing. Inside the parentheses we would be changing to the new folder location of the file and the new file's name. This change to the script would be mandatory for a new project. There could be other changes based on the structure of the provided data. One of which being a change to the column indexes if the candidate names column is second and the county names is third. <img width="239" alt="Election-Audit-data-columns" src="https://user-images.githubusercontent.com/114922260/199112531-15bcca47-0261-4f56-8560-b40f6a3a5be5.png"> Then we would have to change candidate_name = row[2] to row[1] and county_name from [2] to [1]. 
