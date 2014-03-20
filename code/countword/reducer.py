#!/usr/bin/python

import sys

# dictionary to store the counts
wc = {}

# read input from STDIN
# We assume that Hadoop sends values for multiple keys to one reducer.

for line in sys.stdin:
	line = line.strip ()
	# We used the tab as the separator in mapper output
	# For correctness we want only one split
	word, count = line.split ('\t', 1)

	# As Hadoop passes strings, we need to convert the count into an integer.
	try:
		count = int (count)
	except ValueError:
		continue

	if word not in wc:
		wc[word] = count
	else:
		wc[word] = wc[word] + count
		

for word, count in wc.items ():
	print '%s\t%s' % (word, count)

