# TODO: pseudo code before beginning

#import modules

import os
import csv

#set path

csvpath = os.path.join(".", "Resources", "election_data.csv")
output_path = os.path.join(".", "Analysis", "Poll_Analysis_Jake.txt")
#print(csvpath)

#initialize variables

total_votes = 0
Correy_votes = 0
Khan_votes = 0
Li_votes = 0
Otooley_votes = 0
Correy_percent = 0
Khan_percent = 0
Li_percent = 0
Otooley_percent = 0




#open csv file

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Header
    csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")

    for row in csv_reader:

        #find total votes
        total_votes = total_votes + 1

        #find votes for each candidate
        if row[2] == "Correy":
            Correy_votes = Correy_votes + 1

        elif row[2] == "Khan":
            Khan_votes = Khan_votes + 1

        elif row[2] == "Li":
            Li_votes = Li_votes + 1

        #rest to Otooley 
        else:
            Otooley_votes = Otooley_votes +1

    #find percent of votes

    Correy_percent = round((Correy_votes/total_votes)*100,3)

    Khan_percent = round((Khan_votes/total_votes)*100,3)

    Li_percent = round((Li_votes/total_votes)*100,3)

    Otooley_percent = round((Otooley_votes/total_votes)*100,3)

        
#use dictionary to find candidate with max votes

Candidate_dic = {
    "Winner: Correy": Correy_votes,
    "Winner: Khan": Khan_votes,
    "Winner: Li": Li_votes,
    "Winner: Otooley": Otooley_votes
}

max_key= max(Candidate_dic, key=Candidate_dic.get)

#print(max_key)





#test work with prints

# print(total_votes)
# print(Correy_votes)
# print(Khan_votes)
# print(Li_votes)
# print(Otooley_votes)
# print()
# print(max_key)

# print(Correy_percent)
# print(Khan_percent)
# print(Li_percent)
# print(Otooley_percent)


output = (

f"Election Results\n"
f"------------------------------------\n"
f"Total Votes: {total_votes}\n"
f"------------------------------------\n"
f"Khan: {Khan_percent}%    {Khan_votes} votes\n"
f"Correy: {Correy_percent}%   {Correy_votes} votes\n"
f"Li:   {Li_percent}%     {Li_votes} votes\n"
f"O'Tooley: {Otooley_percent}%  {Otooley_votes} votes\n"
f"------------------------------------\n"
f"{max_key}\n"
f"------------------------------------\n"
)


print(output)
#export results to txt file

with open(output_path, "w") as txt_file:
    txt_file.write(output)
