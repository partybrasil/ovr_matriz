from core.plugin_manager import CorePluginManager
import psutil
import uuid
import random
from rich.console import Console
from rich.table import Table

app_context = {
    "role": "admin",
    "protocol": "none",
    # Puedes agregar más parámetros globales aquí
}

plugin_manager = CorePluginManager(app_context)
plugin_manager.auto_register_plugins()

console = Console()

def list_network_adapters():
    adapters = psutil.net_if_addrs()
    return list(adapters.keys())

def show_adapters():
    adapters = psutil.net_if_addrs()
    table = Table(title="Adaptadores de Red Disponibles")
    table.add_column("Nombre")
    table.add_column("Direcciones")
    for name, addrs in adapters.items():
        ips = ", ".join([a.address for a in addrs if a.family.name in ("AF_INET", "AF_INET6")])
        table.add_row(name, ips)
    console.print(table)

def create_virtual_adapter(name=None, protocol="Ethernet", fake_mac=None, properties=None):
    # Placeholder: La creación real depende del SO y requiere privilegios de administrador
    # Ejemplo de implementación real (comentada):
    #   - En Windows: usar netsh o PowerShell para crear adaptador TAP o Loopback.
    #   - En Linux: usar ip tuntap add, ip link, etc.
    #   - En macOS: usar ifconfig para crear interfaces virtuales.
    # Aquí deberías invocar comandos del sistema para crear el adaptador real.
    # Por ejemplo:
    # import subprocess
    # subprocess.run(["ip", "tuntap", "add", "dev", name, "mode", "tun"])
    # subprocess.run(["ip", "link", "set", name, "up"])
    # subprocess.run(["ip", "link", "set", name, "address", fake_mac])
    if not name:
        name = f"VirtualAdapter_{uuid.uuid4().hex[:6]}"
    if not fake_mac:
        fake_mac = "02:00:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(4))
    # Simulación de creación
    console.print(f"[bold green]Adaptador virtual '{name}' creado con MAC {fake_mac} y protocolo {protocol}.[/bold green]")
    return name

def select_adapter_interactive():
    while True:
        show_adapters()
        console.print("\nOpciones: [1] Conectar a existente  [2] Modificar existente  [3] Crear nuevo  [q] Salir")
        opt = console.input("Elige una opción: ")
        if opt == "1":
            adapters = list_network_adapters()
            for idx, name in enumerate(adapters):
                console.print(f"{idx+1}. {name}")
            sel = int(console.input("Selecciona el número del adaptador: ")) - 1
            return adapters[sel]
        elif opt == "2":
            adapters = list_network_adapters()
            for idx, name in enumerate(adapters):
                console.print(f"{idx+1}. {name}")
            sel = int(console.input("Selecciona el número del adaptador a modificar: ")) - 1
            # Aquí podrías pedir nuevas propiedades y simular la modificación
            console.print(f"Propiedades modificadas para {adapters[sel]}.")
            return adapters[sel]
        elif opt == "3":
            name = console.input("Nombre del nuevo adaptador: ")
            protocol = console.input("Protocolo (Ethernet/WiFi/VPN): ")
            fake_mac = console.input("MAC falsa (opcional): ") or None
            # Aquí podrías pedir más propiedades y filtros
            return create_virtual_adapter(name, protocol, fake_mac)
        elif opt.lower() == "q":
            return None

def get_connection_info(adapter_name):
    adapters = psutil.net_if_addrs()
    addrs = adapters.get(adapter_name, [])
    ips = [a.address for a in addrs if a.family.name in ("AF_INET", "AF_INET6")]
    # Simulación de info extra
    protocols = ["TCP", "UDP"]
    estado = "Conectado"
    nivel_seguridad = "Alto"
    caracteristicas = ["Firewall", "VPN"]
    conectado_a = "Servidor remoto"
    ips_remotas = ["203.0.113.1"]
    return {
        "yo": "Usuario",
        "mis_ips": ips,
        "adaptador": adapter_name,
        "protocolos": protocols,
        "estado": estado,
        "seguridad": nivel_seguridad,
        "caracteristicas": caracteristicas,
        "conectado_a": conectado_a,
        "ips_remotas": ips_remotas
    }

def show_connection_header(info):
    table = Table(title="Estado de la Conexión", show_header=False)
    table.add_row("Yo", info["yo"])
    table.add_row("Mis IPs", ", ".join(info["mis_ips"]))
    table.add_row("Adaptador", info["adaptador"])
    table.add_row("Protocolos", ", ".join(info["protocolos"]))
    table.add_row("Estado", info["estado"])
    table.add_row("Nivel de Seguridad", info["seguridad"])
    table.add_row("Características", ", ".join(info["caracteristicas"]))
    table.add_row("Conectado a", info["conectado_a"])
    table.add_row("IPs Remotas", ", ".join(info["ips_remotas"]))
    console.clear()
    console.print(table)

def main():
    # Inicialización de la app
    adapter = select_adapter_interactive()
    if adapter:
        info = get_connection_info(adapter)
        show_connection_header(info)
        # Aquí puedes continuar con la lógica de la app usando el adaptador seleccionado
    # ...existing code...

if __name__ == "__main__":
    main()