import json

# Cargar datos desde el archivo JSON
def cargar_datos():
    with open("ej2.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

# 1️⃣ ¿Cuántas pruebas de idiomas hay en el documento?
def contar_pruebas(pruebas):
    return len(pruebas)

# 2️⃣ Pruebas que duran más de dos horas
def pruebas_largas(pruebas):
    return [prueba["Titulo"] for prueba in pruebas if prueba["Horas"] > 2]

# 3️⃣ URLs de pruebas "No Presencial"
def urls_no_presencial(pruebas):
    return [prueba["URL"] for prueba in pruebas if "No Presencial" in prueba["TipoFormacion"]]

# 4️⃣ Obtener título y profesores de una prueba por ID
def prueba_por_id(pruebas, id_prueba):
    for prueba in pruebas:
        if prueba["ID"] == id_prueba:
            return {"Titulo": prueba["Titulo"], "Profesores": [prof["NombreCompleto"] for prof in prueba["Profesorado"]]}
    return None

# 5️⃣ Título y profesores de todas las pruebas
def titulos_y_profesores(pruebas):
    return {prueba["Titulo"]: [prof["NombreCompleto"] for prof in prueba["Profesorado"]] for prueba in pruebas}

# 6️⃣ Fechas de inicio y fin de todas las pruebas
def fechas_de_pruebas(pruebas):
    return {prueba["ID"]: {"Inicio": prueba["InicioImparticion"], "Fin": prueba["FinImparticion"]} for prueba in pruebas}

# 7️⃣ Pruebas de más de 3 horas y presenciales
def pruebas_presenciales_largas(pruebas):
    return [prueba["Titulo"] for prueba in pruebas if prueba["Horas"] > 3 and "Presencial" in prueba["TipoFormacion"]]

# 8️⃣ Cantidad de pruebas por tipo de formación
def pruebas_por_tipo(pruebas):
    conteo = {"Presencial": 0, "No Presencial": 0}
    for prueba in pruebas:
        if "Presencial" in prueba["TipoFormacion"]:
            conteo["Presencial"] += 1
        elif "No Presencial" in prueba["TipoFormacion"]:
            conteo["No Presencial"] += 1
    return conteo

# 9️⃣ Prueba más corta y más larga
def pruebas_extremos(pruebas):
    prueba_corta = min(pruebas, key=lambda x: x["Horas"])
    prueba_larga = max(pruebas, key=lambda x: x["Horas"])
    return {
        "Más corta": {"Titulo": prueba_corta["Titulo"], "Horas": prueba_corta["Horas"]},
        "Más larga": {"Titulo": prueba_larga["Titulo"], "Horas": prueba_larga["Horas"]}
    }

# 🔟 Pruebas que empiezan o terminan en una fecha dada
def pruebas_por_fecha(pruebas, fecha):
    return [prueba["Titulo"] for prueba in pruebas if prueba["InicioImparticion"].startswith(fecha) or prueba["FinImparticion"].startswith(fecha)]

# 1️⃣1️⃣ Pruebas con profesores que contienen una palabra en su nombre
def pruebas_por_nombre_profesor(pruebas, palabra):
    return [prueba["Titulo"] for prueba in pruebas if any(palabra.lower() in prof["NombreCompleto"].lower() for prof in prueba["Profesorado"])]

# 1️⃣2️⃣ Detalles de una prueba por título
def detalles_por_titulo(pruebas, titulo):
    for prueba in pruebas:
        if prueba["Titulo"] == titulo:
            return prueba
    return None

# Cargar datos
pruebas = cargar_datos()

# Pruebas de las funciones
print("Cantidad de pruebas:", contar_pruebas(pruebas))
print("Pruebas que duran más de 2 horas:", pruebas_largas(pruebas))
print("URLs de pruebas No Presenciales:", urls_no_presencial(pruebas))
print("Datos de la prueba con ID 'A15050163':", prueba_por_id(pruebas, "A15050163"))
print("Títulos y profesores de todas las pruebas:", titulos_y_profesores(pruebas))
print("Fechas de todas las pruebas:", fechas_de_pruebas(pruebas))
print("Pruebas presenciales de más de 3 horas:", pruebas_presenciales_largas(pruebas))
print("Cantidad de pruebas por tipo:", pruebas_por_tipo(pruebas))
print("Prueba más corta y más larga:", pruebas_extremos(pruebas))
print("Pruebas en la fecha '2015-01-09':", pruebas_por_fecha(pruebas, "2015-01-09"))
print("Pruebas con profesor que contiene 'María':", pruebas_por_nombre_profesor(pruebas, "María"))
print("Detalles de la prueba 'Inglés - Prueba de nivel - Para cursos segundo cuatrimestre':", detalles_por_titulo(pruebas, "Inglés - Prueba de nivel - Para cursos segundo cuatrimestre"))
