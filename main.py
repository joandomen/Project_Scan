## 🔥 **Archivo Principal: `main.py`**
import threading
from detection_arp import arp_scan
from port_scan import scan_ports
from network_graph import generate_network_graph

def network_scan(network, ports):
    print("Escaneando la red...\n")
    devices = arp_scan(network)
    if not devices:
        print("No se encontraron dispositivos.")
        return
    results = []
    threads = []
    for device in devices:
        ip = device["ip"]
        mac = device["mac"]
        def scan_and_store():
            open_ports = scan_ports(ip, ports)
            results.append({"ip": ip, "mac": mac, "ports": open_ports})
            print(f"IP: {ip}\t MAC: {mac}\t Puertos abiertos: {open_ports}")
        thread = threading.Thread(target=scan_and_store)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    with open("resultados_ports.txt", "w") as f:
        for result in results:
            f.write(f"IP: {result['ip']}\t MAC: {result['mac']}\t Puertos abiertos: {result['ports']}\n")
    generate_network_graph(results)

if __name__ == "__main__":
    target_network = "192.168.1.0/24"  # Ajusta según tu red
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389]
    network_scan(target_network, common_ports)