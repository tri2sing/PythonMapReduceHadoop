#!/usr/bin/python

import sys

total = 0
previous_link = False

for line in sys.stdin:
	line = line.strip ()
	current_link, count = line.split ('\t', 1)
	try:
		count = int (count)
	except ValueError:
		continue

	if previous_link and current_link != previous_link:
		print '%s\t%i' % (previous_link, total)
		previous_link = current_link
		total = count
	else:
		previous_link = current_link
		total += count

# last link
print '%s\t%i' % (previous_link, total)
