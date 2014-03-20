#!/usr/bin/python

import sys

total = 0
previous_subject = False

for line in sys.stdin:
	line = line.strip ()
	current_subject, count = line.split ('\t', 1)
	try:
		count = int (count)
	except ValueError:
		continue

	if previous_subject and current_subject != previous_subject:
		print '%s\t%i' % (previous_subject, total)
		previous_subject = current_subject
		total = count
	else:
		previous_subject = current_subject
		total += count

# last subject
print '%s\t%i' % (previous_subject, total)
