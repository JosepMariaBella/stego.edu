from scapy.all import *

dest = "172.20.121.11"
paquet = IP(dst=dest) / ICMP() / "hello world"

send(paquet)
