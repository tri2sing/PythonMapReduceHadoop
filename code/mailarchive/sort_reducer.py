#!/usr/bin/python

import sys

# read input from STDIN
for line in sys.stdin:
	line = line.strip ()
	count, subject = line.split ('\t', 1)
	print '%s\t%s' % (subject, count)


