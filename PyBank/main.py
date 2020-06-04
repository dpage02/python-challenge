import os 
import csv 

# read in the file
    # create month and value variables
# total number of months in dataset
# net total amount of Profits/Losses
# greatest increase/decrease over the entire period

# read in the file
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    # reading the header first
    header = next(csvreader)

    # getting count
    #count = len(list(csvreader))
    #print(count)

    # getting net profit and count
    net= 0
    months_count = 0
    greatest_inc = 0
    greatest_dec = 0
   
    for row in csvreader:
        months_count += 1
        net += int(row[1])
        
        change = int(row[1])
        if change > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]

    print(greatest_inc_month,greatest_inc)  