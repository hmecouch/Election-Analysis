counties = ("Arapahoe", "Denver", "Jefferson")
if counties[1] == "Denver":
    print(counties[1])

if "El Paso" in counties: 
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties.")


if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#prints keys in dictionary

for county in counties_dict:
    print(county)
print(" ")

for county in counties_dict.keys():
    print(county)
print(" ")

#prints values in dictionary

for voters in counties_dict.values():
    print(voters)
print(" ")

for county in counties_dict:
    print(counties_dict[county])
print(" ")

for county in counties_dict:
    print(counties_dict.get(county))
print(" ")

#print key-value pair

for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                 {"county":"Denver", "registered_voters": 463353},
                 {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
print(" ")
# iterate over the list of dictionaries using range() to get counties

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

print(" ")
#to retrieve only the values from each dictionary we need a nested loop

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#print on county name

for county_dict in voting_data:
    print(county_dict['county'])

#f-string example

print(f"{counties[1]} IS A BIG CITY" )
# variables and expressions go in curly braces


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

#f strings can print multiple string or lines to the screen

candidate_votes = int(input("how many votes did the candidate get? "))

total_votes = int(input("what is the total number of votes? "))

message_to_candidate = (
    f"You recieved {candidate_votes:,} votes. "
    f"The total votes was {total_votes:,}. "
    f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#format the floating point
# f'{value:{width}.{precision}}' decimal places
# f'{value:{width},.{precision}}' adds comma for thousands seperator

#skill drill

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']:,} voters.")
                
        

        

    

        


