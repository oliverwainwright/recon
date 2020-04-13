#!/usr/bin/python3

import ipaddress
import socket
import re
import time
import subprocess

#rev2 = (ipaddress.ip_address('146.20.151.112').reverse_pointer.split('in-addr.arpa'))
#rev2[0] + 'zen.spamhaus.org'


net = ipaddress.ip_network('208.75.120.0/30')
#net = ipaddress.ip_network('205.140.240.0/24')
for host in net.hosts():
#	print(host)
	rev_ip = (ipaddress.ip_address(host).reverse_pointer.split('in-addr.arpa'))
	for blacklist in [ "spam.dnsbl.sorbs.net", "b.barracudacentral.org", "dnsbl.sorbs.net", "bl.spamcop.net" ]:
#		rev_ip[0] + 'spam.dnsbl.sorbs.net'
		print(rev_ip[0] + blacklist)
		ip = re.findall("^127.", socket.gethostbyname(rev_ip[0] + blacklist))
		time.sleep(1.2)
		if (ip):
			print("Bad Host Found " + str(host) + " in " + blacklist)
#		else:
#			print("OK: x")
