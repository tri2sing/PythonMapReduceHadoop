#!/usr/bin/python

import sys
linkcount = {}

for line in sys.stdin:
	line = line.strip ()
	link, count = line.split ('\t', 1)
	try:
		count = int (count)
	except ValueError:
		continue

	if link not in linkcount:
		linkcount[link] = count
	else:
		linkcount[link] = linkcount[link] + count
		
for link, count in linkcount.items ():
	print '%s\t%s' % (link, count)

