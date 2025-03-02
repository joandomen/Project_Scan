### 🔹 **`detection_arp.py`** (Escaneo ARP)

import scapy.all as scapy

def arp_scan(network):
    arp_request = scapy.ARP(pdst=network)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return [{"ip": element[1].psrc, "mac": element[1].hwsrc} for element in answered_list]