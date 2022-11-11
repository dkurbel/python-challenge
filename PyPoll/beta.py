# import modules

import os
import csv

# define filepath

csvpath = os.path.join('Resources', 'election_data.csv')

# define variables
total_votes = 0
candidates = {}


# open file

with open(csvpath) as readfile:
    df = csv.reader(readfile)
    next(df)

# parse data

    for row in df:

        # add to total votes

        total_votes +=1

        # create new key if not in dictionary

        if row[2] not in candidates:
            candidates[row[2]] = 0

        # add +1 to value according to matching key in dictionary

        if row[2] in candidates:
            candidates[row[2]] = candidates[row[2]] + 1

    winner = max(candidates, key=candidates.get)
            

# display analysis in terminal

    print(f'''

Election Results

--------------------------

Total Votes: {total_votes}

--------------------------

''')

    for x, y in candidates.items():
        print(f'{x}: {y} ({y/total_votes * 100}%)')

    print(f'''

--------------------------

Winner: {winner}

''')

    # define writing file path

    output_path = os.path.join('analysis', 'results.txt')

    # write to text file

    with open(output_path, 'w') as writefile:
        writefile.write(f'''

Election Results

--------------------------

Total Votes: {total_votes}

--------------------------

''')

        for x, y in candidates.items():
            writefile.write(f'''
{x}: {y} ({y/total_votes * 100}%) \n
''')

        writefile.write(f'''

--------------------------

Winner: {winner}

''')