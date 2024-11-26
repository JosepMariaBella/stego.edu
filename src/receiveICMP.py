from scapy.all import sniff, ICMP

# Define a callback function that processes each packet
def icmp_packet_callback(packet):
    if packet.haslayer(ICMP):
        # Get the payload of the ICMP packet
        icmp_payload = packet[ICMP].payload.load if packet[ICMP].payload else b''

        if icmp_payload:
            print(f"ICMP packet payload: {icmp_payload.decode(errors='ignore')}")  # Decode payload as string

# Capture ICMP packets (use appropriate interface or adjust filter)
sniff(filter="icmp", prn=icmp_packet_callback, store=0)
