import scapy.all as scapy

#1) arp_request
#2) broadcast
#3) response

arp_request_packet = scapy.ARP()
#scapy.ls(scapy.ARP())
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#scapy.ls(scapy.Ether())
combined_packet = broadcast_packet/arp_request_packet
result=scapy.srp(combined_packet, timeout=1)
print(result)