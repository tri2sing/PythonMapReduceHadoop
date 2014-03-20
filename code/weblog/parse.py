import re
from datetime import datetime

# ("([^\\s]+) - - \\[(.+)\\] \"([^\\s]+) (/[^\\s]*) HTTP/[^\\s]+\" [^\\s]+ ([0-9]+)")

line = 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985'
#line = '199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 4179'

pattern = re.compile ("([^\\s]+) - - \\[(.+)\\] \"([^\\s]+) (/[^\\s]*) HTTP/[^\\s]+\" [^\\s]+ ([0-9]+)")
match = pattern.match (line)

print line
print match.group(5)

print '\n'
i = 1
for group in match.groups():
	print '[%d]: %s' % (i, group)
	i += 1

dt = datetime.strptime (match.group(2), '%d/%b/%Y:%H:%M:%S -0400')
print dt.hour
