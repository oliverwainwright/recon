#!/usr/bin/python3

import ipaddress
import socket
import re
import time
import subprocess

with open('allow.txt', 'rt') as f:
	for i in f:
		line = i.rstrip('\r\n')
		if re.search("/", line):
#			print('net ', line)
			net = ipaddress.ip_network(line)
#			print('net ', net)
			for host in net.hosts():
				rev_ip = (ipaddress.ip_address(host).reverse_pointer.split('in-addr.arpa'))

				for blacklist in [ "spam.dnsbl.sorbs.net", "b.barracudacentral.org", "dnsbl.sorbs.net", "bl.spamcop.net" ]:
					print(rev_ip[0] + blacklist)
					ip = re.findall("^127.", socket.gethostbyname(rev_ip[0] + blacklist))
					time.sleep(1.2)
					if (ip):
						print("Bad Host Found " + str(host) + " in " + blacklist)

		else:
			rev_ip = (ipaddress.ip_address(line).reverse_pointer.split('in-addr.arpa'))
			print("rev_ip is ", rev_ip)
			for blacklist in [ "spam.dnsbl.sorbs.net", "b.barracudacentral.org", "dnsbl.sorbs.net", "bl.spamcop.net" ]:
				rev_host = rev_ip[0] + blacklist
				print("rev_host is ", rev_host)
				#nsLookupResult = subprocess.run(["/usr/bin/host", rev_host], shell=True)
				nsLookupResult = subprocess.check_output(["/usr/bin/host", rev_host])
				nsLookupResult = nsLookupResult.decode('ASCII')
				print("nsLookupResult ", nsLookupResult)
				ip = re.findall("127.", nsLookupResult)
				print('ip is ', ip)
				time.sleep(1.2)
				if (ip):
					print("Bad Host Found " + str(line) + " in " + blacklist)
