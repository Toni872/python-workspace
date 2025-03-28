import os
import json

def crear_listin():
    """Crea el fichero listin.txt si no existe."""
    if not os.path.exists("listin.txt"):
        with open("listin.txt", "w") as f:
            pass

def consultar_telefono(nombre):
    """Consulta el teléfono de un cliente por su nombre."""
    with open("listin.txt", "r") as f:
        for linea in f:
            cliente, telefono = linea.strip().split(",")
            if cliente == nombre:
                return telefono
    return "Cliente no encontrado"

def agregar_cliente(nombre, telefono):
    """Añade un nuevo cliente al listín."""
    with open("listin.txt", "a") as f:
        f.write(f"{nombre},{telefono}\n")

def eliminar_cliente(nombre):
    """Elimina a un cliente del listín."""
    encontrado = False
    with open("listin.txt", "r") as f:
        lineas = f.readlines()
    
    with open("listin.txt", "w") as f:
        for linea in lineas:
            if linea.strip().split(",")[0] != nombre:
                f.write(linea)
            else:
                encontrado = True
    
    return "Cliente eliminado" if encontrado else "Cliente no encontrado"

def ejecutar_comando(opcion, args):
    """Ejecuta una opción sin interacción directa del usuario."""
    if opcion == "1":
        return consultar_telefono(args[0])
    elif opcion == "2":
        agregar_cliente(args[0], args[1])
        return "Cliente agregado."
    elif opcion == "3":
        return eliminar_cliente(args[0])
    elif opcion == "4":
        return "Salir"
    else:
        return "Opción no válida."

def cargar_comandos(desde_archivo="comandos.json"):
    """Carga los comandos desde un archivo JSON."""
    if os.path.exists(desde_archivo):
        with open(desde_archivo, "r") as f:
            return json.load(f)
    return []

# Ejemplo de uso sin input interactivo
def main():
    crear_listin()
    comandos = cargar_comandos()
    
    for opcion, args in comandos:
        resultado = ejecutar_comando(opcion, args)
        print(f"Resultado ({opcion}): {resultado}")

if __name__ == "__main__":
    main()
