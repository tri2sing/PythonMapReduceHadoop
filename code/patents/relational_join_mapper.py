#!/usr/bin/python

import os
import sys

full_path = os.environ['map_input_file']
short_name = full_path.split('/')[-1]

for line in sys.stdin:
	# remove any leading or trailing whitespace
	line = line.strip()
	# The two short file names are citations and patents.
	# Both files are comma separated: citations has two columns, and patents has more.
	# Split the line into two parts using the first comma as the separator.
	key, value = line.split(',', 1)
	# Create a new value which has a new separator and has the file name as prefix.
	value = short_name + '#' + value
	# write to STDOUT a tab-delimited string
	print '%s\t%s' % (key, value)


