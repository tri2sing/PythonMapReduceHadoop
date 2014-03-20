#!/usr/bin/python

import sys

def output_join (key, ctns, pats):
	# If there are no keys in citations then there are no joins to be performed
	if not ctns:
		return	
	# If there are no keys in patents then there are no joins to be performed
	if not pats:
		return
	
	# If there are key from both sources then perform a cross product
	for c in ctns:
		for p in pats:
			print '%s,%s' % (key, c+p)
	
# Each reducer will receive only data for one key
# We will use that fact to perform the inner join.

ctnlist = []
patlist = []
prev_key = None

for line in sys.stdin:
	line = line.strip ()
	#print line
	cur_key, value = line.split ('\t', 1)
	filename, remainder = value.split ('#', 1)
	#print '%s-%s-%s' % (cur_key, filename, remainder)

	if prev_key and prev_key != cur_key:
		output_join (prev_key, ctnlist, patlist)
		prev_key = cur_key
		ctnlist = []
		patlist = []
		if (filename == 'citations'):
			ctnlist.append(remainder)
		else:
			patlist.append(remainder)
	else:
		prev_key = cur_key
		if (filename == 'citations'):
			ctnlist.append(remainder)
		else:
			patlist.append(remainder)
		
output_join (prev_key, ctnlist, patlist)

