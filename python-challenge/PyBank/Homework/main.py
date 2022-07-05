import os
import csv

# read the CSV file to get the data from
file = os.path.join("..","Resources", "budget_data.csv")
with open(file,'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
    header = next(csvreader)
    
    # create lists for the month count, net profit, and changes in profit from month to month 
    month_count = []
    profit = []
    change_profit = []
    
                      
    # loop through the lists created from the CSV to get the number of months and the net profit 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
# create variables for the greatest increase and greatest decrease
greatestIncrease = max(change_profit)
greatestDecrease = min(change_profit)

# grab the corresponding date for greatest increase and greatest decrease
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(greatestIncrease))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(greatestDecrease))})")      

# output a text file in the 'analysis' folder
financial_analysis = os.path.join('..','analysis', 'financial_analysis.txt')
with open(financial_analysis,"w") as text:
    text.write("Financial Analysis")
    text.write("\n")
    text.write("------------------------")
    text.write("\n")
    text.write(f"Total Months:{len(month_count)}")
    text.write("\n")
    text.write(f"Total: ${sum(profit)}")
    text.write("\n")
    text.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    text.write("\n")
    text.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(greatestIncrease))})")
    text.write("\n")
    text.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(greatestDecrease))})")