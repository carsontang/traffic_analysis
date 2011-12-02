#! /usr/bin/python

import csv
import sys

THRESHOLD = 8.0
DEFAULT_DURATION = 200.0

csvFilename = sys.argv[1]
outputFilename = sys.argv[2]
outputFile = open(outputFilename, 'w')

data = csv.reader(open(csvFilename, 'rb'))
for row in data:
	start_time = float(row[10])
	duration = float(row[11])
	if duration > THRESHOLD:
		duration = DEFAULT_DURATION

	outputFile.write(str(start_time) + "," + str(duration) + "\n")	
