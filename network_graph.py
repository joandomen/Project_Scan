### 🔹 **`network_graph.py`** (Generación de Topología de Red)
import networkx as nx
from pyvis.network import Network

def generate_network_graph(devices):
    G = nx.Graph()
    for device in devices:
       G.add_node(device["ip"], label=f"{device['ip']}\n{device['mac']}")
    net = Network(height="500px", width="800px")
    net.from_nx(G)
    net.show("grafo_ports.html", notebook=False)
