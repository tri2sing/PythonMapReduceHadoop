#!/usr/bin/python

import sys
import re

#199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
pattern = re.compile ("([^\\s]+) - - \\[(.+)\\] \"([^\\s]+) (/[^\\s]*) HTTP/[^\\s]+\" [^\\s]+ ([0-9]+)")
for line in sys.stdin:
	line = line.strip()
	match = pattern.match (line)
	if (match is not None):
		print '%s\t%s' % (match.group(4), 1)
