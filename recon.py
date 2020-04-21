#!/usr/bin/python3

import ipaddress
import random
import re
import time
import subprocess

# open for output naughty hosts to file
badBoys = open("badBoys.txt", "w")

# read sort -u combined dnsbl into an array
with open('sorted_bigDnsbl.txt', 'rt') as d:
	# define empty array
	dnsbl_array = []
	for j in d:
		# strip newline from array member
		dnsbl = j.rstrip('\n')
		# push object onto array
		dnsbl_array.append(dnsbl)

# myBlacklist function
def myBlacklist(ipAddress):
	# get reverse ip address and drop in-addr.arpa
	rev_ip = (ipaddress.ip_address(ipAddress).reverse_pointer.split('in-addr.arpa'))

	for blacklist in dnsbl_array:
		# append blocklist domain to reverse ip address	
		rev_host = rev_ip[0] + blacklist

		# test command execution
		try:
			nsLookupResult = subprocess.check_output(["/usr/bin/host", rev_host], stderr=subprocess.STDOUT, timeout=5)
		# if command fails
		except subprocess.CalledProcessError as err:
			return_code = err.returncode
			nsLookupResult = err.output
		# if command timesout
		except subprocess.TimeoutExpired as err:
			nsLookupResult = err.output

		# nsLookupResult will be None or Null of command timed out
		if (nsLookupResult == None):
			nsLookupResult = "SERVER FAIL ," + rev_host
		else:
			nsLookupResult = nsLookupResult.decode('ASCII')
			# checking for valid host ip address
			ip = re.findall("127.", nsLookupResult)

			sleepTime = random.uniform(0,3)
			time.sleep(sleepTime)

		# if nsLookup contains /^127./, then we found a naughty host
		if (ip):
			print("Bad Host Found " + str(ipAddress) + " in " + blacklist)
			badBoys.write("Bad Host Found " + str(ipAddress) + " in " + blacklist + "\n")

# read ip address allow list, conists of host ip addresses an cidr notation networks
with open('test.txt', 'rt') as f:
	for i in f:
		# strip newline from array member
		line = i.rstrip('\r\n')
		# determine if ip address is host or cidr block
		if re.search("/", line):
			net = ipaddress.ip_network(line)

			# pass cidr block to hosts() and loop through entire cidr block
			for host in net.hosts():
				myBlacklist(host)
		else:
				myBlacklist(line)

badBoys.close()
