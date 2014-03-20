#!/usr/bin/python

import sys

total = 0
previous_hour = False

for line in sys.stdin:
	line = line.strip ()
	current_hour, count = line.split ('\t', 1)
	try:
		count = int (count)
	except ValueError:
		continue

	if previous_hour and current_hour != previous_hour:
		print '%s\t%i' % (previous_hour, total)
		previous_hour = current_hour
		total = count
	else:
		previous_hour = current_hour
		total += count

# last key
print '%s\t%i' % (previous_hour, total)
