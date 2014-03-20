#!/usr/bin/python

import sys

for line in sys.stdin:
	# remove any leading or trailing whitespace
	line = line.strip()
	key, value = line.split ('\t', 1)
	print '%s\t%s' % (key, value)

