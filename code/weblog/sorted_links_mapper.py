#!/usr/bin/python

import sys
import re

pattern = re.compile ("([^\\s]+) - - \\[(.+)\\] \"([^\\s]+) (/[^\\s]*) HTTP/[^\\s]+\" [^\\s]+ ([0-9]+)")
for line in sys.stdin:
	line = line.strip()
	match = pattern.match (line)
	if (match is not None):
		print '%s\t%s' % (match.group(4), 1)
