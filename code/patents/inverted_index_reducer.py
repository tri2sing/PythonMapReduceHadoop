#!/usr/bin/python

import sys

citers_list = []
previous_cited = False

for line in sys.stdin:
	line = line.strip ()
	current_cited, citer = line.split ('\t', 1)

	if previous_cited and current_cited != previous_cited:
		print '%s\t%s' % (previous_cited, str(citers_list))
		previous_cited = current_cited
		citers_list = []
		citers_list.append(citer)
	else:
		previous_cited = current_cited
		citers_list.append(citer)

# last list
print '%s\t%s' % (previous_cited, str(citers_list))
