#!/usr/bin/python

import sys
import parsembox


for record in parsembox.get_record (sys.stdin):
	print '%s\t%s' % (record['subject'], 1)
