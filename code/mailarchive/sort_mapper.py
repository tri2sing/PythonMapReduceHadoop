#!/usr/bin/python

import sys

for line in sys.stdin:
	# remove any leading or trailing whitespace
	line = line.strip()
	# split the line into words using tab as the separator
	subject, count = line.split ('\t', 1)
	# write to STDOUT a tab-delimited string
	print '%s\t%s' % (count, subject)

