import os
import csv

#create a path
fname="Resources/election_data.csv"
outputfile = "election_analysis.txt"

#set the variables
vote_list = []
candidate_list = []
percent_candidate = []
total_candidate = []

#totalvote = 0

with open(fname, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
        vote_list.append(row[2])

totalvote = len(vote_list)
print(totalvote)

for name in vote_list:
    if name not in candidate_list:
        candidate_list.append(name)

#total for each canidate


khan_total = 0
otooley_total = 0
li_total = 0
correy_total = 0

for candidate in candidate_list:
    for vote in vote_list:
        
        if candidate == 'Khan' and vote=='Khan':
            khan_total += 1
          
        if candidate == "O'Tooley" and vote=="O'Tooley":
            otooley_total += 1
 
        if candidate == 'Li' and vote=='Li':
            li_total += 1

        if candidate == 'Correy' and vote=='Correy':
            correy_total += 1        

# print('Khan', khan_total)
# print("O'Tooley",  otooley_total)
# print('Li', li_total)
# print('Correy', correy_total)

pct_khan = round((khan_total / totalvote * 100), 2)
pct_otooley = round((otooley_total / totalvote * 100), 2)
pct_li = round((li_total / totalvote * 100), 2)
pct_correy = round((correy_total / totalvote * 100), 2)

winner = max([(pct_khan,'Khan'),(pct_otooley, "O'Tooley"),(pct_li, "Li"),(pct_correy, "Correy")])



print("election results")
print("________________________________")
print(f'total votes: {totalvote}')
print("________________________________")
print(f'Winner: {winner[1]}')
print("_________________________________")
print(f'Khan:  {pct_khan}%  {khan_total}')
print(f"O'Tooley:  {pct_otooley}%  {otooley_total}")
print(f'Li:  {pct_li}%  {li_total}')
print(f'Correy:  {pct_correy}%  {correy_total}')





#output file
with open (outputfile, 'w') as output:
     output.write('Election results\n')
     output.write("----------------------\n")
     output.write(f"Total votes {totalvote}\n")
     output.write("----------------------\n")
     output.write(f'Khan:  {pct_khan}%  {khan_total}\n')
     output.write(f"O'Tooley:  {pct_otooley}%  {otooley_total}\n")
     output.write(f'Li:  {pct_li}%  {li_total}\n')
     output.write(f'Correy:  {pct_correy}%  {correy_total}\n')
     output.write("----------------------\n")
     output.write(f'Winner: {winner[1]}')






        


