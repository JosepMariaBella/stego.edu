from scapy.all import  *
from netfilterqueue import NetfilterQueue


# UFW: -A ufw-before-output -o enp0s3 -p icmp -j NFQUEUE --queue-num 1
def process_packet(pkt):
    # Convierte el paquete nfqueue a un objeto Scapy
    scapy_packet = IP(pkt.get_payload())
#    scapy_packet.show()
    payload = scapy_packet[ICMP].load
    msg = "bon dia"
    msg_bytes = msg.encode('utf-8')
    payload = payload + msg_bytes
    del scapy_packet[IP].chksum
    del scapy_packet[ICMP].chksum
    del scapy_packet[IP].len
    scapy_packet[ICMP].load = payload

#    scapy_packet = scapy_packet.__class__(bytes(scapy_packet))
#    print(f"payload : {scapy_packet.show()}")
    scapy_packet.show()
    pkt.set_payload(bytes(scapy_packet))

    pkt.accept()

def main():
    # Crear una instancia de nfqueue
    q = NetfilterQueue()
    #q = netfilterqueue.NetfilterQueue()
    q.bind(1, process_packet)  # Vinculamos a la cola 1

    try:
        q.run()
    except KeyboardInterrupt:
        print('\nInterrupted')
    finally:
        q.unbind()

if __name__ == "__main__":
    main()
