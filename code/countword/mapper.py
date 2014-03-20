#!/usr/bin/python

import sys

for line in sys.stdin:
	# remove any leading or trailing whitespace
	line = line.strip()
	# split the line into words using space as teh separator
	words = line.split()
	# write to STDOUT a tab-delimited string
	for word in words:
		print '%s\t%s' % (word, 1)

