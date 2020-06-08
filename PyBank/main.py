import os 
import csv 

# read in the file
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    # reading the header first
    header = next(csvreader)
    next_line = next(csvreader)

    # needed variables 
    net= 0
    months_count = 0
    greatest_inc = 0
    greatest_dec = 0
    values = []
    change =[]

    for row in csvreader:

        # getting months count
        months_count += 1

        # getting net total 
        net += int(row[1])
        
        # adding value to dict
        values.append(row[1])

       

    # printing statements 
    print("Finacial Analysis")
    print("------------------------------------")
    print(f"Total Months: {months_count}")
    print(f"Total: ${net}")
    print(f"Average Change: ")
    print(f"Greatest Increase in Profits:")
    print(f"Greatest Decrease in Profits:")

output_path = os.path.join("Analysis","PyBankAanlysis.txt")
with open(output_path,'w') as txtfile:
     # printing statements to output file 
    txtfile.write("Finacial Analysis")
    txtfile.write("\n------------------------------------")
    txtfile.write(f"\nTotal Months: {months_count}")
    txtfile.write(f"\nTotal: ${net}")
    txtfile.write(f"\nAverage Change: ")
    txtfile.write(f"\nGreatest Increase in Profits:")
    txtfile.write(f"\nGreatest Decrease in Profits:")