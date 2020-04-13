#!/usr/bin/python3

import ipaddress
import socket

#rev2 = (ipaddress.ip_address('146.20.151.112').reverse_pointer.split('in-addr.arpa'))
#rev2[0] + 'zen.spamhaus.org'


net = ipaddress.ip_network('208.75.120.0/24')
for x in net.hosts():
#	print(x)
	rev_ip = (ipaddress.ip_address(x).reverse_pointer.split('in-addr.arpa'))
#	rev_ip[0] + 'spam.dnsbl.sorbs.net'
	print(rev_ip[0] + 'spam.dnsbl.sorbs.net')
#	socket.gethostbyname(rev_ip[0] + 'spam.dnsbl.sorbs.net')
