from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    # Extract and display information for IP packets
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        payload = str(packet[IP].payload).strip()

        # Protocol mapping
        protocol_map = {
            1: 'ICMP',
            6: 'TCP',
            17: 'UDP',
        }
        protocol_name = protocol_map.get(protocol, 'Unknown')

        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol_name}")
        print(f"Payload: {payload[:50]}")  # Display the first 50 characters of payload
        print("-" * 50)

def start_sniffing(interface=None):
    # Start sniffing on the specified network interface or all interfaces
    print("Starting packet capture...")
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    # Specify the network interface if needed, e.g., "eth0", "wlan0"
    start_sniffing()
