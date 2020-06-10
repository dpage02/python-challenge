import os 
import csv 

# read in the file
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    # reading the header first
    header = next(csvreader)
    

    # needed variables 
    net= 0
    months_count = 0
    values = []
    change =[]
    months = []

    for row in csvreader:

        # getting months count
        months_count += 1

        # getting net total 
        net += int(row[1])
        
        # adding value to dict
        values.append(row[1])
        months.append(row[0])

    for i in range(len(values)-1):
        last_month = int(values[i])
        this_month = int(values[i+1])
        profit = this_month-last_month
        change.append(profit)
    
    # getting greatest inc/dec values
    greatest_inc = max(change)
    greatest_dec = min(change)
    # finding months
    inc_month_index = change.index(greatest_inc)
    inc_month = months[inc_month_index + 1]
    dec_month_index = change.index(greatest_dec)
    dec_month = months[dec_month_index + 1]

    # getting average change
    avg_change= f"{(sum(change)/len(change)+1):.2f}"
    #print(avg_change)

    # printing statements 
    print("Finacial Analysis")
    print("------------------------------------")
    print(f"Total Months: {months_count}")
    print(f"Total: ${net}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits:{inc_month} (${greatest_inc})")
    print(f"Greatest Decrease in Profits:{dec_month} (${greatest_dec})")

output_path = os.path.join("Analysis","PyBankAanlysis.txt")
with open(output_path,'w') as txtfile:
     # printing statements to output file 
    txtfile.write("Finacial Analysis")
    txtfile.write("\n------------------------------------")
    txtfile.write(f"\nTotal Months: {months_count}")
    txtfile.write(f"\nTotal: ${net}")
    txtfile.write(f"\nAverage Change: ${avg_change}")
    txtfile.write(f"\nGreatest Increase in Profits: {inc_month} (${greatest_inc})")
    txtfile.write(f"\nGreatest Decrease in Profits: {dec_month} (${greatest_dec})")