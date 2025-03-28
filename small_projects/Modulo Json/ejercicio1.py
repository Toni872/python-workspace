import json

# Cargar datos desde el archivo JSON
def cargar_datos():
    with open("ej1.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos["bookstore"]["book"]

# 1️⃣ ¿Cuántos libros hay en la librería?
def contar_libros(libros):
    return len(libros)

# 2️⃣ Mostrar libros cuyo precio esté en un intervalo
def libros_por_precio(libros, limite_inferior, limite_superior):
    return [libro["title"]["__text"] for libro in libros if limite_inferior <= float(libro["price"]) <= limite_superior]

# 3️⃣ Buscar libros cuyo título empiece con una cadena dada
def buscar_por_titulo(libros, cadena):
    return [(libro["title"]["__text"], libro["year"]) for libro in libros if libro["title"]["__text"].startswith(cadena)]

# 4️⃣ Obtener todos los títulos con sus autores
def titulos_con_autores(libros):
    return {libro["title"]["__text"]: libro["author"] for libro in libros}

# 5️⃣ Libros de una categoría específica
def libros_por_categoria(libros, categoria):
    return [libro["title"]["__text"] for libro in libros if libro["_category"] == categoria]

# 6️⃣ Autores de un libro específico
def autores_por_titulo(libros, titulo):
    for libro in libros:
        if libro["title"]["__text"] == titulo:
            return libro["author"] if isinstance(libro["author"], list) else [libro["author"]]
    return []

# 7️⃣ Libro con el precio más alto
def libro_mas_caro(libros):
    libro_caro = max(libros, key=lambda libro: float(libro["price"]))
    return libro_caro["title"]["__text"], libro_caro["price"]

# 8️⃣ Libros publicados en un año específico
def libros_por_anio(libros, anio):
    return [libro["title"]["__text"] for libro in libros if libro["year"] == str(anio)]

# 9️⃣ Libros con múltiples autores
def libros_con_multiples_autores(libros):
    return [libro["title"]["__text"] for libro in libros if isinstance(libro["author"], list)]

# 🔟 Actualizar precio de un libro
def actualizar_precio(libros, titulo, nuevo_precio):
    for libro in libros:
        if libro["title"]["__text"] == titulo:
            libro["price"] = str(nuevo_precio)
            with open("ej1.json", "w", encoding="utf-8") as archivo:
                json.dump({"bookstore": {"book": libros}}, archivo, indent=4, ensure_ascii=False)
            return f"Precio de '{titulo}' actualizado a {nuevo_precio}."
    return "Libro no encontrado."

# 1️⃣1️⃣ Eliminar un libro dado su título
def eliminar_libro(libros, titulo):
    libros_filtrados = [libro for libro in libros if libro["title"]["__text"] != titulo]
    with open("ej1.json", "w", encoding="utf-8") as archivo:
        json.dump({"bookstore": {"book": libros_filtrados}}, archivo, indent=4, ensure_ascii=False)
    return f"Libro '{titulo}' eliminado."

# 1️⃣2️⃣ Mostrar títulos y años ordenados por año de publicación
def libros_ordenados_por_anio(libros):
    return sorted([(libro["title"]["__text"], libro["year"]) for libro in libros], key=lambda x: x[1])

# 1️⃣3️⃣ Libros con precio por debajo del promedio
def libros_bajo_precio_promedio(libros):
    precios = [float(libro["price"]) for libro in libros]
    promedio = sum(precios) / len(precios)
    return [libro["title"]["__text"] for libro in libros if float(libro["price"]) < promedio]

# Cargar datos
libros = cargar_datos()

# Pruebas de las funciones
print("Cantidad de libros:", contar_libros(libros))
print("Libros entre $20 y $40:", libros_por_precio(libros, 20, 40))
print("Libros que empiezan con 'Harry':", buscar_por_titulo(libros, "Harry"))
print("Títulos con autores:", titulos_con_autores(libros))
print("Libros en la categoría 'WEB':", libros_por_categoria(libros, "WEB"))
print("Autores de 'Harry Potter':", autores_por_titulo(libros, "Harry Potter"))
print("Libro más caro:", libro_mas_caro(libros))
print("Libros publicados en 2005:", libros_por_anio(libros, 2005))
print("Libros con múltiples autores:", libros_con_multiples_autores(libros))
print(actualizar_precio(libros, "Harry Potter", 25.99))
print(eliminar_libro(libros, "Everyday Italian"))
print("Libros ordenados por año:", libros_ordenados_por_anio(libros))
print("Libros por debajo del precio promedio:", libros_bajo_precio_promedio(libros))
