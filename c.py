#!/usr/bin/python3

import ipaddress
import random
import re
import time
import subprocess

with open('sorted_bigDnsbl.txt', 'rt') as d:
	dnsbl_array = []
	for j in d:
		dnsbl = j.rstrip('\n')
		dnsbl_array.append(dnsbl)

with open('allow.txt', 'rt') as f:
	for i in f:
		line = i.rstrip('\r\n')
		if re.search("/", line):
#			print('net ', line)
			net = ipaddress.ip_network(line)
#			print('net ', net)
			for host in net.hosts():
				rev_ip = (ipaddress.ip_address(host).reverse_pointer.split('in-addr.arpa'))

				for blacklist in dnsbl_array:
					print('blacklist is ', blacklist)	
					
					#for blacklist in [ "spam.dnsbl.sorbs.net", "b.barracudacentral.org", "dnsbl.sorbs.net", "bl.spamcop.net" ]:
					rev_host = rev_ip[0] + blacklist
#					print("rev_host is ", rev_host)

					try:
						nsLookupResult = subprocess.check_output(["/usr/bin/host", rev_host], stderr=subprocess.STDOUT, timeout=5)
					except subprocess.CalledProcessError as err:
						return_code = err.returncode
						nsLookupResult = err.output
					except subprocess.TimeoutExpired as err:
						nsLookupResult = err.output

					if (nsLookupResult == None):
						nsLookupResult = "SERVER FAIL ," + rev_host
					else:
						nsLookupResult = nsLookupResult.decode('ASCII')
#						print("1 nsLookupResult ", nsLookupResult)
						ip = re.findall("127.", nsLookupResult)
#						print('ip is ', ip)

					sleepTime = random.uniform(0,3)
					time.sleep(sleepTime)
					if (ip):
						print("Bad Host Found " + str(host) + " in " + blacklist)
		else:
			rev_ip = (ipaddress.ip_address(line).reverse_pointer.split('in-addr.arpa'))
#			print("rev_ip is ", rev_ip)
			#for blacklist in [ "spam.dnsbl.sorbs.net", "b.barracudacentral.org", "dnsbl.sorbs.net", "bl.spamcop.net" ]:
			for  blacklist in dnsbl_array:
				print('blacklist is ', blacklist)	
				rev_host = rev_ip[0] + blacklist
#				print("rev_host is ", rev_host)

				try:
					#nsLookupResult = subprocess.check_output(["/usr/bin/host", rev_host], stderr=subprocess.STDOUT)
					nsLookupResult = subprocess.check_output(["/usr/bin/host", rev_host], stderr=subprocess.STDOUT, timeout=5)
				except subprocess.CalledProcessError as err:
					return_code = err.returncode
					nsLookupResult = err.output
				except subprocess.TimeoutExpired as err:
					nsLookupResult = err.output

				if (nsLookupResult == None):
					nsLookupResult = "SERVER FAIL ," + rev_host
				else:
					nsLookupResult = nsLookupResult.decode('ASCII')
#					print("1 nsLookupResult ", nsLookupResult)
					ip = re.findall("127.", nsLookupResult)
#					print('ip is ', ip)

				sleepTime = random.uniform(0,3)
				time.sleep(sleepTime)
				if (ip):
					print("Bad Host Found " + str(line) + " in " + blacklist)
