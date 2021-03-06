#!/usr/bin/python3

import ipaddress
import random
import re
import time
import subprocess
import ipinfo
import whois
import pprint
import logging

# basic logging config
logging.basicConfig(level = logging.INFO, filename="badBoys.log", format = '%(asctime)s.%(msecs)03d %(levelname)s:\t %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode = 'w')
logger = logging.getLogger()

# ipinfo access token
access_token = '023b29ecb0b39c'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()

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
			ip_line = "Bad Host Found " + str(ipAddress) + " in " + blacklist
			print(ip_line)
			logging.info(ip_line)

def myipInfo(ipAddress):
	ipAddress = str(ipAddress)
	details = handler.getDetails(ipAddress)
	
	# testing to see if details.hostname exists
	try:
		hostname = details.hostname
	except:
		hostname = ""

	try:
		org = details.org
	except:
		org = ""
	try:
		city = details.city
	except:
		city = ""
	try:
		region = details.region
	except:
		region = ""
	try:
		country_name = details.country_name
	except:
		country_name = ""
	try:
		postal = details.postal
	except:
		postal = ""
	
	print("hostname is ", hostname)

	# testing to see if whois.query(hostname) returns valid domain
	if ".ch"==hostname[-3:]:
		domain = ""
		registrar = ""
		creationDate = ""
		expireDate = ""
		lastUpdated = ""
		domainName = ""
	else:
		domain = whois.query(hostname)
		try:
			registrar = domain.registrar
		except:
			registrar = ""
		try:
			creationDate = domain.creation_date.strftime('%m/%d/%y %I:%M %S %p')
		except:
			creationDate = ""
		try:
			expireDate = domain.expiration_date.strftime('%m/%d/%y %I:%M %S %p')
		except:
			expireDate = ""
		try:
			lastUpdated = domain.last_updated.strftime('%m/%d/%y %I:%M %S %p')
		except:
			lastUpdated = ""
		try:
			domainName = domain.name
		except:
			domainName = ""

	myipInfo_tuple = (ipAddress, hostname, domainName, org, city, region, country_name, postal, registrar, creationDate, expireDate, lastUpdated)

	myipInfo_line = ",".join(myipInfo_tuple)
	print(myipInfo_line)
	logging.info(myipInfo_line)

# THIS IS THE MAINLINE
# read combo ip address block + allow list, consists of host ip addresses an cidr notation networks
with open('block_allow.txt', 'rt') as f:
	for i in f:
		# strip newline from array member
		line = i.rstrip('\r\n')
		# determine if ip address is host or cidr block
		if re.search("/", line):
			net = ipaddress.ip_network(line)

			# pass cidr block to hosts() and loop through entire cidr block
			for host in net.hosts():
			
				myipInfo(host)
				myBlacklist(host)
		else:
				myipInfo(line)
				myBlacklist(line)

