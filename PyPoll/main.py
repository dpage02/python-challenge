import os 
import csv

# read in the file
polling_csv = os.path.join("Resources","election_data.csv")
with open(polling_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    # reaer header first and going to next line
    header = next(csvreader)
    
    # variables 
    total_votes = 0 
    Khan_votes = 0 
    Correy_votes = 0
    Li_votes = 0
    Otooley_votes = 0 

    # create dictionary to keep names and vote total 
    vote_dict = {}

    # start loop through csv
    for row in csvreader:

        #to get total votes
        total_votes += 1

        # to get individual vote counts
        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        else :
            Otooley_votes += 1
    
    # addind names: votes to dictionary 
    vote_dict["Khan"] = Khan_votes
    vote_dict["Correy"] = Correy_votes
    vote_dict["Li"] = Li_votes
    vote_dict["O'Tooley"] = Otooley_votes
    
     # getting percentages 
    khan_percentage = f"{((Khan_votes/total_votes) * 100):.2f}"
    correy_percentage = (Correy_votes/total_votes)*100
    li_percenatage = (Li_votes/total_votes)*100
    otooley_percentage = (Otooley_votes/total_votes)*100


    # Getting most votes number
    values = vote_dict.values()
    most_votes = max(values)
    # Getting name out of dictionary 
    for name, votes in vote_dict.items():
        if most_votes == votes:
            winner = name

    # printing statements
    print("Election Results")
    print("-----------------------")
    print(f"Total votes: {total_votes}") 
    print("-----------------------")
    print(f"Khan: {khan_percentage}% ({Khan_votes})")
    print(f"Correy: {correy_percentage}% ({Correy_votes})")
    print(f"Li: {li_percenatage}% ({Li_votes})")
    print(f"O'Tooley: {otooley_percentage}% ({Otooley_votes})")
    print("-----------------------")
    print(f"Winner: {winner}")
    print("-----------------------")

output_path = os.path.join("Analysis","PyPollAanlysis.txt")
with open(output_path,'w') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\n-----------------------")
    txtfile.write(f"\nTotal votes: {total_votes}") 
    txtfile.write("\n-----------------------")
    txtfile.write(f"\nKhan: {khan_percentage}% ({Khan_votes})")
    txtfile.write(f"\nCorrey: {correy_percentage}% ({Correy_votes})")
    txtfile.write(f"\nLi: {li_percenatage}% ({Li_votes})")
    txtfile.write(f"\nO'Tooley: {otooley_percentage}% ({Otooley_votes})")
    txtfile.write("\n-----------------------")
    txtfile.write(f"\nWinner: {winner}")
    txtfile.write("\n-----------------------")