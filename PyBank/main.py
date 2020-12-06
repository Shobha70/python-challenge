# import the os module
import os

# import module for reading CSV files
import csv

# file path
budgetdatafilepath = os.path.join('Resources', 'budget_data.csv')

# open csv file
with open(budgetdatafilepath) as csvfile:

    # read csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row and skip
    csv_header = next(csvreader)

    # initialize lists   
    fadate = []
    fapl = []
    faplchange = []

    # Read each row of data after the header
    for row in csvreader:

        # build lists for Month-year and profit-loss
        fadate.append(row[0])
        fapl.append(int(row[1]))

    # build list for change
    for i in range(len(fapl)):
        if i == 0:
            faplchange.append(0)
        else:
            faplchange.append(fapl[i] - fapl[i-1])    

    # count totalmonths 
    totalmonths = len(fadate)
    # add profit-loss
    nettotal = sum(fapl)
    # find average change
    averagePLchange = round(sum(faplchange)/(totalmonths-1),2)
    # find min change
    minPLchange = min(faplchange)
    # find max change
    maxPLchange = max(faplchange)
    #find month with min change  
    minPLmonth = fadate[faplchange.index(minPLchange)]
    # find month with max change
    maxPLmonth = fadate[faplchange.index(maxPLchange)]   
       
# Print to Terminal...
print('Financial Analysis\n---------------------------------------------------------------------------------------------')
print(f'TotalMonths: {totalmonths}')
print(f'Total: ${nettotal}')
print(f'Average Change: {averagePLchange}')
print(f'Greatest Increase in Profits: {maxPLmonth} (${maxPLchange})')
print(f'Greatest Decrease in Profits: {minPLmonth} (${minPLchange})')
print('-----------------------------------------------------------------------------------------------')


# Print to file
# Specify the file to write to
output_path = os.path.join("Analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as outputfile:

    # Write rows
    outputfile.write('Financial Analysis\n---------------------------------------------------------------------------------------------')
    outputfile.write(f'\nTotalMonths: {totalmonths}')
    outputfile.write(f'\nTotal: ${nettotal}')
    outputfile.write(f'\nAverage Change: {averagePLchange}')
    outputfile.write(f'\nGreatest Increase in Profits: {maxPLmonth} (${maxPLchange})')
    outputfile.write(f'\nGreatest Decrease in Profits: {minPLmonth} (${minPLchange})')
    outputfile.write('\n-----------------------------------------------------------------------------------------------')