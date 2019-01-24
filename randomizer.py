# a randomizer for bike shop stuff
import csv
from random import  shuffle

# input file - must be utf-8 format
file = 'pbcList.csv'

# output randomized file - must premake file
newOrder = 'newOrder.csv'
pbcList =[]
with open(file,'r', newline = '') as csvfile:
    reader = csv.reader(csvfile, dialect = 'unix')
    first = next(reader)
    for row in reader:
        pbcList += [row]

    shuffle(pbcList)
with open(newOrder,'w') as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerow(first)
    for item in pbcList:
        writer.writerow(item)
