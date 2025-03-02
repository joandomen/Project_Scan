### 🔹 **`port_scan.py`** (Escaneo de Puertos)
import socket

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        s.close()
    return open_ports