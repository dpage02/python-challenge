import os 
import csv

# read in the file
polling_csv = os.path.join("Resources","election_data.csv")
with open(polling_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    # reaer header first and going to next line
    header = next(csvreader)

    total_votes = 0 
    canidates = []
    votes = []
    candidate_vote_dict ={}

    for row in csvreader:

        total_votes += 1

        if row[2] not in canidates:
            canidates.append(row[2])
        
        votes.append(row[2])
        
    for name in canidates:
        vote_counter = votes.count(name)

        vote_percentage = f"{((vote_counter/total_votes)*100):.3f}"
        candidate_vote_dict[name] = [vote_counter, vote_percentage]
    
    winner = max(candidate_vote_dict, key=candidate_vote_dict.get)
    #winning_votes = max(candidate_vote_dict.values())
    
    
    print("Election Results")
    print("--------------------")
    print(f"Total votes: {total_votes}")
    print("--------------------")
    for name, values in candidate_vote_dict.items():
        print(f"{name}: {values[1]}% ({values[0]})")
    print("--------------------")
    print(f"Winner: {winner}")
    print("--------------------")


output_path = os.path.join("Analysis", "PyPollAnalysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\n--------------------")
    txtfile.write(f"\nTotal votes: {total_votes}")
    txtfile.write("\n--------------------")
    for name, values in candidate_vote_dict.items():
        txtfile.write(f"\n{name}: {values[1]}% ({values[0]})")
    txtfile.write("\n--------------------")
    txtfile.write(f"\nWinner: {winner}")
    txtfile.write("\n--------------------")