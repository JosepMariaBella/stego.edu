def captura_icmp(packet):

    if ICMP in packet:
        ip_dst = packet[ICMP].show()
        payload = packet[ICMP].payload
    print(f" IP Desti: {ip_dst}")
    print(f" Payload: {payload}")
    packet[ICMP].payload = "bon dia"
    send(packet)


if __name__ == "__main__":
    sniff(filter="icmp and ip src 172.20.120.10", prn = captura_icmp)
