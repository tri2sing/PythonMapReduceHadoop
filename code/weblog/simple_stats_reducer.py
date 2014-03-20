#!/usr/bin/python

import sys

total = 0.0
count = 0
min = 0
max = 0

for line in sys.stdin:
	line = line.strip ()
	key, value = line.split ('\t', 1)
	try:
		value = int (value)
	except ValueError:
		continue

	count += 1
	total = total + value
	if (value < min):
		min = value
	if (value > max):
		max = value

print '%s\t%s' % ('Min', min)
print '%s\t%s' % ('Max', max)
print '%s\t%s' % ('Count', count)
print '%s\t%s' % ('Mean', int(total/count))

