import os 
import csv 
from datetime import datetime 

# read in the file
budget_csv = os.path.join("employee_data.csv")
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    # reading the header first
    header = next(csvreader)

    first_names = []
    last_names = []
    birthdate = []
    for row in csvreader:

        emp_id = row[0]

        full_name = row[1]
        first_name, last_name = full_name.split(" ",1)
        first_names.append(first_name)

        birthdate_original = row[2]
        #birthdate_original = datetime.strptime(birthdate_original,'%Y/%m/%d')
        birthdate_new = birthdate_original.strftime('%m/%d/%Y')
        birthdate.append(birthdate_new)


    print(birthdate)