# import modules

import csv
import os

# define the file path

csvpath = os.path.join('Resources', 'budget_data.csv')

# define variables

months = 0
netPL = 0
lastPL = 0
PLchanges = []
Dates = []
line_count = 0

# open file

with open(csvpath) as readfile:

    df = csv.reader(readfile)

    # skip headers

    next(df)

    # parse data

    for row in df:

        # add to month count

        months +=1

        # add Profit/Loss to net profit/loss counter

        netPL += float(row[1])

        # set conditional to check first row

        if line_count == 0:

            # set first value for profit/loss

            lastPL = float(row[1])

            # add to line counter

            line_count += 1

        # condition for all other rows

        else:

            # add difference between current P/L and last P/L to PLchanges

            PLchanges.append(float(row[1])-lastPL)

            # add corresponding date to Dates

            Dates.append(row[0])

            # set current value as lastPL

            lastPL = float(row[1])

            # add to line counter

            line_count +=1

    # find average change in P/L as the mean of PLchanges, conditional to prevent divide by 0

    if float(len(PLchanges)) != 0:
        averagePL = sum(PLchanges) / float(len(PLchanges))
    else:
        averagePL = 'undeterminable'

    # find the greatest increase in p/l and the date

    maxprofit = max(PLchanges)
    maxdate = Dates[PLchanges.index(maxprofit)]

    # find the greatest decrease in p/l and the date

    minprofit = min(PLchanges)
    mindate = Dates[PLchanges.index(minprofit)]

    # print results into terminal

    print(f'''
Total number of months: {months}

Net total profit/losses: {netPL}

Changes in P/L over entire set:

{PLchanges}

Average change in P/L: {averagePL}

The greatest increase in profits was ${maxprofit} during {maxdate}.

The greatest decrease in profits was ${minprofit} during {mindate}.''')

    # define writing file path

    output_path = os.path.join('analysis', 'results.txt')

    # open and write into file

    with open(output_path, 'w') as writefile:
        writefile.write(f'''
The total number of months included in the dataset is {months}.

The net total amount of profit/losses is {netPL}.

The changes in profit/losses over time are as follows:
{PLchanges}

The average change in profit/losses is {averagePL}.

The greatest increase in profits was ${maxprofit} during {maxdate}.

The greatest decrease in profits was ${minprofit} during {mindate}.
''')