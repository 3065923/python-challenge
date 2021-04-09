# TODO: pseudo code before beginning

#import modules

import os
import csv

#set path
csvpath = os.path.join(".", "Resources", "budget_data.csv")
output_path = os.path.join(".", "Analysis", "Bank_Analysis_Jake.txt")
print(csvpath)
#initialize variables

total_months = 0
total_profit = 0
total_losses = 0
profit_change = 0
average_change = 0
max_date = ["String"]
greatest_inc = ["", 0]
greatest_dec = ["", 9999999999]

    #also looking for average change

change_list= []

#open csv file

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Header
    csv_header = next(csv_reader)
  #  print(f"Header: {csv_header}")

    #prev_row = [0]     *** variable does not need to be a list
    prev_row = 0
    #max_date = 0

    #find total months using for to go through rows and add
    for row in csv_reader:

        total_months = total_months + 1

        #add second column up to find total profit and losses
        total_profit = total_profit + int(row[1])            


        #find average change of Profit/Losses
        #append to a list and find average of list


        if total_months <= 1:
            pass

            

        else:
            
            #ave_change =
            change = int(row[1]) - int(prev_row)
            change_list.append(change)

            if change > greatest_inc[1]:
                greatest_inc[0] = row[0]

                greatest_inc[1]= change
            
            if change < greatest_dec[1]:
                greatest_dec[0] = row[0]

                greatest_dec[1]= change


            #change_list.append(int(row[1]) - int(row-1[1]))

        prev_row = int(row[1])


                #max_change = max(change_list)
    

 #   for row in csv_reader:
if row[1] == int(max(change_list)):
            max_date[0]= str(row[0])

else:
    pass


average_change = round((sum(change_list) / len(change_list)), 2)


print()
print()


#Show me the money
#print(max_date)
print(max(change_list))
#, str(row[0])}")
print(min(change_list))

output = (

f"Financial Analysis\n"
f"------------------------------------\n"
f"Total Months: {total_months}\n"
f"Total Profit ${total_profit:,.0f}\n"
f"Greatest Increase: {greatest_inc[0]}  ${greatest_inc[1]:,.0f}\n"
f"Greatest Decrease:  {greatest_dec[0]}  ${greatest_dec[1]:,.0f}\n"
f"Average Change: ${average_change:,.2f}\n"
)


print(output)
#export results to txt file

with open(output_path, "w") as txt_file:
    txt_file.write(output)



