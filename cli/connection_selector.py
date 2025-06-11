def select_connection_type():
    print("Selecciona tipo de conexión:")
    options = [
        "1. P2P Directo",
        "2. P2P NAT Traversal",
        "3. Cliente-Servidor",
        "4. Malla (Mesh)",
        "5. Hub-and-Spoke",
        "6. Broadcast/Multicast Virtualizado"
    ]
    for opt in options:
        print(opt)
    choice = input("Opción: ")
    return choice
