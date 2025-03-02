<<<<<<< HEAD
# 🔍 Project_Scan - Análisis y Escaneo de Red

🚀 **Project_Scan** es una potente herramienta diseñada para el escaneo de redes y la detección de puertos abiertos en dispositivos conectados. Utiliza técnicas avanzadas de escaneo **ARP** y **TCP** para proporcionar una visión detallada de la infraestructura de red.

---

## 📌 Características Principales
✔️ Detección rápida de dispositivos en la red mediante ARP.  
✔️ Escaneo de puertos abiertos en cada dispositivo encontrado.  
✔️ Visualización de la topología de la red en un **gráfico interactivo**.  
✔️ Resultados detallados guardados en archivos de texto para su análisis.  
✔️ Fácil instalación y uso en entornos **Windows**, **Linux**, y **MacOS**.  

---

## 📂 Estructura del Proyecto
```
Project_Scan/
├── modules/                # Contiene módulos como detection_arp.py, port_scan.py, etc.
├── main.py                 # Archivo principal que ejecuta el escaneo
├── requirements.txt        # Lista de dependencias necesarias
├── resultados_ports.txt    # Archivo donde se guardan los resultados del escaneo
├── grafo_ports.html        # Visualización en HTML de la topología de la red
```

---

## 🛠️ Instalación y Configuración
### 🔹 1. Clona el repositorio:
```bash
git clone https://github.com/joandomen/Project_Scan.git
cd Project_Scan
```

### 🔹 2. Crea un entorno virtual y actívalo:
**Linux / MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 🔹 3. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

---

## 🚀 Uso de la Herramienta
Para ejecutar el escaneo de red y detección de puertos abiertos, simplemente ejecuta:
```bash
python main.py
```
📌 **Resultados:**  
✔️ La lista de dispositivos detectados y sus puertos abiertos se guardará en `resultados_ports.txt`.  
✔️ La topología de la red se generará en `grafo_ports.html` como una visualización interactiva.  

---

## 📢 Notas Importantes
🔹 **Permisos:** Asegúrate de ejecutar el script con los permisos adecuados para acceder a la red.  
🔹 **Windows:** Es recomendable usar **WSL** (Windows Subsystem for Linux) para un mejor rendimiento.  
🔹 **Modo Administrador:** En algunos sistemas, es necesario ejecutar como administrador para escanear puertos.  

---

## 📜 Licencia
Este proyecto está bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles.

💡 **Contribuciones y sugerencias son bienvenidas**. Si tienes ideas para mejorar **Project_Scan**, ¡no dudes en colaborar! 🚀
=======
# Project_Scan
Mini proyecto para escaner redes y puertos
>>>>>>> 9da467531030a1ec555f1974946dce064884e0f0
