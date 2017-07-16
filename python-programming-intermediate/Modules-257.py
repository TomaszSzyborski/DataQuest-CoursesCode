## 1. Introduction to Modules ##


import math
root = math.sqrt(99)
flr = math.floor(89.9)

## 2. Importing Using An Alias ##


import math as m
root = m.sqrt(33)

## 3. Importing A Specific Object ##


from math import *

root = sqrt(1001)

## 4. Variables Within Modules ##

import math

print(math.pi)
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)

## 5. The CSV Module ##

import csv
f = open("nfl.csv", 'r')
csvreader = csv.reader(f)
nfl = list(csvreader)

## 6. Counting How Many Times a Team Won ##


# First, import the CSV module
import csv
# Then, open our file in `r` mode
f = open("nfl.csv", "r")
# Use the csv module to read the file, and convert the result
# to a list
nfl = list(csv.reader(f))

# Start our count at 0
patriots_wins = 0
# Loop through our data set, counting the rows with "New England Patriots"
# as the winner
for row in nfl:
    if row[2] == "New England Patriots":
        patriots_wins += 1

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(team):
    count = 0
    for row in nfl:
        if row[2] == team:
            count = count + 1
    return count

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")