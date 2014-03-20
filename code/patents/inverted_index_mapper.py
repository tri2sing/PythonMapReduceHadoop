#!/usr/bin/python

import sys

for line in sys.stdin:
	# remove any leading or trailing whitespace
	line = line.strip()
	# split the line into two parts using comma as the separator
	citer, cited = line.split(',', 1)
	# write to STDOUT a tab-delimited string
	print '%s\t%s' % (cited, citer)


