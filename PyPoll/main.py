# import the os module
import os

# import module for reading CSV files
import csv

# file path
electiondatafilepath = os.path.join('Resources', 'election_data.csv')

# open csv file
with open(electiondatafilepath) as csvfile:

    # read csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row and skip
    csv_header = next(csvreader)

    # initialize lists and dictionary 
    voterid = []
    county = []
    candidate = []
    popularvotesbycandidate= {}

    # Read each row of data after the header
    for row in csvreader:

        # build lists for voterid, county, and candidate
        voterid.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])

    print(f'Election Results\n----------------------------------------------------------------------')

    # Count totalvotes
    Totalvotes = len(voterid)
    print(f'Total Votes: {Totalvotes}')

    print(f'----------------------------------------------------------------------\n')

    # get unique candidates
    uniquecandidates = set(candidate)
    
    # Loop through each candidate
    for c in uniquecandidates:
        totalvotesbycandidate = 0
        for cand in candidate:
            if c == cand:
                totalvotesbycandidate += 1
        popularvotesbycandidate[c] = (f'{round(((totalvotesbycandidate/Totalvotes)*100),2):.3f}% ({totalvotesbycandidate})')
        print(f'{c}: {round(((totalvotesbycandidate/Totalvotes)*100),2):.3f}% ({totalvotesbycandidate})')
        
            
print(f'----------------------------------------------------------------------\n')
winner = max(popularvotesbycandidate, key=popularvotesbycandidate.get)
print(f'Winner: {winner}')
print(f'----------------------------------------------------------------------\n')


# Print to file
# Specify the file to write to
output_path = os.path.join("Analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as outputfile:

    # Write rows
    outputfile.write('Election Results\n---------------------------------------------------------------------------------------------')
    outputfile.write(f'\nTotal Votes: {Totalvotes}')
    outputfile.write('\n-----------------------------------------------------------------------------------------------')
    for keys, values in popularvotesbycandidate.items():
        outputfile.write(f'\n{keys}: {values}')
    outputfile.write('\n-----------------------------------------------------------------------------------------------')
    outputfile.write(f'\nWinner: {winner}')
    outputfile.write('\n-----------------------------------------------------------------------------------------------')