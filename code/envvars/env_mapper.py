#!/usr/bin/python

import os
import sys

#keys = str(os.environ.keys())
full_path = os.environ['map_input_file']
short_name = full_path.split('/')[-1]

for line in sys.stdin:
	# remove any leading or trailing whitespace
	line = line.strip()
	#print '%s\t%s' % (line, keys)
	print '%s\t%s' % (line, short_name)

