import csv

# pull main directory
from pathlib import Path

#pull inform from path
csv_file = Path.cwd() / 'Resources'/'election_data.csv'

#where the file will live
out_file = Path.cwd() /'Analysis'/'election_results.txt'

#open the file.  need a function to open
def election_open():
    if csv_file.exists():
        return open (csv_file)
    else:
        print("file not found")





#define 
def election_results(election_data):
    voter_ID = int(election_data[0])
    county = str(election_data[1])
    canidate = str(election_data[2])
    print(voter_ID)

voter_ID = int(election_data[0])
print(voter_ID)
