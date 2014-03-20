#!/usr/bin/python

# Example data
# 'Date: Fri, 6 Jan 2012 19:12:17 +0100'
# 'From: "Caldarale, Charles R" <Chuck.Caldarale@unisys.com>'
# 'Subject: RE: Different session id per page'
# Example regular expression =  ("([^\\s]+) - - \\[(.+)\\] \"([^\\s]+) (/[^\\s]*) HTTP/[^\\s]+\" [^\\s]+ ([0-9]+)")


# Cleanup
# 201203.mbox - Changed 'Date: lun. 05/03/2012 13:19' to 'Date: 03/05/2012 13:19'
# 201205.mbox - Changed 'Date: Wed, May 16, 2012' to 'Date: Wed, 16 May 2012'
# 201205.mbox - Changed 'Date: Tuesday, May 29, 2012' to 'Date: Tuesday, 29 May 2012'
# 201206.mbox - Changed 'Date: Monday, June 18, 2012' to 'Date: Monday, 18 Jun 2012'
# 201207.mbox - Changed 'Date: Thu, Jul 12, 2012' to ''Date: Thu, 12 Jul 2012'
# 201207.mbox - Changed 'Date: Friday, July 20, 2012' to 'Date: Friday, 20 Jul 2012'
# 201207.mbox - Changed 'Date: Saturday, July 21, 2012' to 'Date: Saturday, 21 Jul 2012'
# 201207.mbox - Changed 'Date: Sunday, July 22, 2012' to 'Date: Sunday, 22 Jul 2012'
# 201208.mbox - Changed 'Date: Fri, Aug 17, 2012' to 'Date: Fri, 17 Aug 2012'
# 201208.mbox - Changed 'Date: 2012/8/17' to 'Date: 8/17/2012'
# 201208.mbox - Changed 'Date: Fri, August 31, 2012' to 'Date: Fri, 31 Aug 2012'
# 201209.mbox - Changed 'Date: Tuesday, September 18, 2012' to 'Date: Tuesday, 18 Sep 2012'
# 201209.mbox - Changed 'Date: Wednesday, September 19, 2012' to 'Date: Wednesday, 18 Sep 2012'
# 201210.mbox - Changed 'Date: Fri, Oct 12, 2012' to ''Date: Fri, 12 Oct 2012'
# 201210.mbox - Changed 'Date: Wednesday, Oct 31, 2012' to ''Date: Wednesday, 31 Oct 2012'
# 201211.mbox - Changed 'Date: Wednesday, November 14, 2012' to ''Date: Wednesday, 14 Nov 2012'
# 201211.mbox - Changed 'Date: Friday, November 16, 2012' to ''Date: Friday, 16 Nov 2012'
# 201211.mbox - Changed 'Date: Wednesday, November 21, 2012' to ''Date: Wednesday, 21 Nov 2012'
# 201211.mbox - Changed 'Date: Saturday, November 24, 2012' to ''Date: Saturday, 24 Nov 2012'
# 201211.mbox - Changed 'Date: Monday, November 26, 2012' to ''Date: Monday, 26 Nov 2012'
# 201212.mbox - Changed 'Date: Tuesday, December 4, 2012' to 'Date: Tuesday, 4 Sep 2012'
# 201212.mbox - Changed 'Date: Thursday, December 20, 2012' to 'Date: Thursday, 20 Sep 2012'
#
# 201210.mbox - :25452,25486s/^/\>/g Was causing defective email address
# 201204.mbox - Joined  46140 'From: =?ISO-8859-1?Q?Miguel_Gonz=E1lez_Casta=F1os?=' and 46141 '<miguel_3_gonzalez@yahoo.es>', 46404 and 46405, 46521 and 46522, 71230 and 71231
# 201204.mbox - Joined all instance of split of 'From: =?UTF-8?B?TWlndWVsIEdvbnrDoWxleiBDYXN0YcOxb3M=?=' and <miguel_3_gonzalez@yahoo.es>
# 201205.mbox - Joined all instance of split of 'From: =?UTF-8?B?TWlndWVsIEdvbnrDoWxleiBDYXN0YcOxb3M=?=' and <miguel_3_gonzalez@yahoo.es>
# 201205.mbox - Joined all instance of split of 'From: =?ISO-8859-1?Q?Miguel_Gonz=E1lez_Casta=F1os?=' and <miguel_3_gonzalez@yahoo.es>'
# 201205.mbox - Joined all instance of split of 'From: =?iso-8859-1?Q?Alexander_Landsnes_Ke=FCl?=' and <Alexander.Landsnes.Keul@visma.no>
# 201206.mbox - =?ISO-8859-1?Q?Miguel_Gonz=E1lez_Casta=F1os?=, =?UTF-8?B?TWlndWVsIEdvbnrDoWxleiBDYXN0YcOxb3M=?=
# 201206.mbox - 18284. Split the Cc to new line
# 201206.mbox - :34185,34190s/^/\>/g and other spots similar changes (:,+3s/^/\>/g).  This was done wherever the replies appended to a message did not have > symbol to mark the original message.
# 201207.mbox - (:,+3s/^/\>/g)
# 201208.mbox - =?UTF-8?B?TWlndWVsIEdvbnrDoWxleiBDYXN0YcOxb3M=?=, =?ISO-8859-1?Q?Miguel_Gonz=E1lez_Casta=F1os?=
# 201209.mbox - From: users-return-236875-STEVEN.J.ADAMUS=3Dsaic.com@tomcat.apache.org (:,+6s/^/\>/g)
# 201210.mbox - From: users-return-237320-STEVEN.J.ADAMUS=3Dsaic.com@tomcat.apache.org (:,+6s/^/\>/g)
# 201211.mbox - From: *Kris Schneider*, From: Sekar, Vasanth=20 (:,+3s/^/\>/g)


import sys
import re

pattern = re.compile ("From .*tomcat.apache.org@tomcat.apache.org.*")
monthtonum = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

def process_date (line):

		try:
			line = line.replace (',', '')
			parts = line.split()
			count = len(parts)
			if count ==5 or count==7 or count==8:
				year = parts[4]
				month = monthtonum[parts[3]]
				day = parts[2]
				if (len(day)==1):
					day = '0' + day
				ret_val = year + '-' + month + '-' + day
			elif count == 4 or count == 3 or count == 2:
				dateparts = parts[1].split('/')
				ret_val = dateparts[2] + '-' + dateparts[0] + '-' + dateparts[1]
			else:
				print line
				print 'Unable to split date'
				sys.exit()
			return ret_val
		except Exception as e:
			print line
			print 'Error processing date'
			print e
			sys.exit ()


def process_subject (line):

		line = line[9:]
		if line.startswith ('RE: ') or line.startswith('Re: '):
			line = line[4:]
		if line.startswith ('[OT] '):
			line = line[5:]
		if line.startswith ('OT: '):
			line = line[4:]
		if line.startswith ('[OT-ish] '):
			line = line[9:]
		if line.startswith ('[ANNOUNCE] '):
			line = line[11:]
		if line.startswith ('[SECURITY] '):
			line = line[11:]
		if line.startswith ('[SOLVED] '):
			line = line[9:]
		if line.startswith ('[ANN] '):
			line = line[6:]

		return line


def process_from (line):

		mark1 = line.find('<')
		if mark1 != -1:
			start = mark1+1
			end = -1
		else:
			mark1 = line.find('[')
			start = mark1 + 8
			mark2 = line.find(']')
			if mark2 != -1:
				end = mark2
			else:
				end = None

		# If the email does not have < or [ as the separator.
		if (mark1 == -1):
			parts = line.split()
			line = parts[1]
			return line

		return line[start:end]


def get_record (input=sys.stdin):
	record = {}
	for line in input:

		try:
			line = line.strip()
			match = pattern.match(line)
	
			if record and match is not None:
				yield record
				record = {}
	
			if line.startswith ('Date: '):
				record['date'] = process_date (line)
				continue
				
			if line.startswith ('Subject: '):
				record['subject'] = process_subject(line)
				continue
	
			if line.startswith ('From: '):
				record['from'] = process_from (line)
				continue

		except Exception as e:
			print line
			print e.args
			sys.exit()

	if record:
		yield record

for record in get_record (sys.stdin):
	print record
