import sys
import struct
import time
from scapy.all import *

n=10000

def send_TCP(i):
	for x in range(i,i+n):
		data = struct.pack('=BHI', 0x12, 20, x)
		pkt = IP(src='192.168.65.145', dst='192.168.65.146')/TCP(sport=10000+i/n,dport=5555)/data
		send(pkt)

def send_UDP(i):
	for x in range(i,i+n):
		data = struct.pack('=BHI', 0x12, 20, x)
		pkt = IP(src='192.168.65.145', dst='192.168.65.146')/UDP(sport=11000+i/n,dport=6666)/data
		send(pkt)

def send_ICMP(i):
	for x in range(i,i+n):
		data = struct.pack('=BHI', 0x12, 20, x)
		pkt = IP(src='192.168.65.145', dst='192.168.65.146')/ICMP()/data
		send(pkt)

threads=[]
times=1
for x in range(times):
	threads.append(threading.Thread(target=send_TCP,args=(x*n,)))
	threads.append(threading.Thread(target=send_UDP,args=(x*n,)))
	threads.append(threading.Thread(target=send_ICMP,args=(x*n,)))


if __name__=='__main__':
	
	time1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	
	for t in threads:
		t.setDaemon(True)
		t.start()
	t.join()
	
	'''
	send_TCP(0)
	send_UDP(0)
	send_ICMP(0)
	'''

	#send_TCP(0)

	print("Finished")
	time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print(time1)
	print(time2)
