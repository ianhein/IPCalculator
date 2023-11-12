import ipaddress

# Solicitar al usuario la clase de dirección IP y los requerimientos de subredes y hosts por subred
direccion_ip_clase = input("Ingrese la clase de dirección IP (A, B, C): ").upper()
subredes_necesarias = int(input("Ingrese el número de subredes necesarias: "))
hosts_por_subred = int(input("Ingrese el número de hosts por subred: "))

# Definir la máscara de subred por defecto basada en la clase de la dirección IP
mascara_por_defecto = {"A": 8, "B": 16, "C": 24}

# Obtener la máscara de subred por defecto para la clase de dirección IP dada
mascara_base = mascara_por_defecto.get(
    direccion_ip_clase, 24
)  # Default a Clase C si no se encuentra

# Calcular el número mínimo de bits requeridos para soportar al menos 'subredes_necesarias' subredes (2^s >= subredes_necesarias)
# y asegurarnos de que la cantidad de hosts soportados (2^(32-mascara_base-s) - 2) sea al menos 'hosts_por_subred'
s = 0  # Número de bits para subredes
while True:
    subredes_posibles = 2**s
    hosts_posibles = (2 ** (32 - mascara_base - s)) - 2
    if subredes_posibles >= subredes_necesarias and hosts_posibles >= hosts_por_subred:
        break
    s += 1

# Calcular la máscara de subred total (bits de la red base + bits prestados para subredes)
mascara_total = mascara_base + s

# Convertir la máscara de subred a formato decimal
mascara_subred_decimal = ipaddress.IPv4Address(
    int("1" * mascara_total + "0" * (32 - mascara_total), 2)
)

# Convertir la máscara de subred a formato binario
mascara_subred_binario_pretty = "1" * mascara_total + "0" * (32 - mascara_total)
mascara_subred_binario_pretty = ".".join(
    mascara_subred_binario_pretty[i : i + 8]
    for i in range(0, len(mascara_subred_binario_pretty), 8)
)

# Mostrar los resultados
print("\n")
print(f"Para la dirección IP de Clase {direccion_ip_clase}:")
print("Número de bits para subredes:", s)
print("Máscara de subred total:", str(mascara_subred_decimal))
print("Máscara de subred en formato binario:", mascara_subred_binario_pretty)
