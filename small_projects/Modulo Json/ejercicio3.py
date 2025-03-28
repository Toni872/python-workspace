import json

# Cargar datos desde el archivo JSON
def cargar_datos():
    with open("ej3.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)["lista"]["provincia"]

# 1️⃣ Obtener todas las provincias
def obtener_provincias(provincias):
    return [prov["nombre"]["__cdata"] for prov in provincias]

# 2️⃣ Obtener todos los municipios (Corrección aplicada)
def obtener_municipios(provincias):
    municipios = []
    for prov in provincias:
        if "localidades" in prov and isinstance(prov["localidades"], dict) and "localidad" in prov["localidades"]:
            localidades = prov["localidades"]["localidad"]
            if isinstance(localidades, dict):  
                municipios.append(localidades["__cdata"])
            elif isinstance(localidades, list):  
                municipios.extend([loc["__cdata"] for loc in localidades])
    return municipios

# 3️⃣ Provincias con el total de municipios
def provincias_con_municipios(provincias):
    return {prov["nombre"]["__cdata"]: 
            len(prov["localidades"]["localidad"]) if "localidades" in prov and isinstance(prov["localidades"]["localidad"], list) else (1 if "localidades" in prov else 0)
            for prov in provincias}

# 4️⃣ Municipios de una provincia dada
def municipios_por_provincia(provincias, nombre_provincia):
    for prov in provincias:
        if prov["nombre"]["__cdata"].lower() == nombre_provincia.lower():
            if "localidades" in prov and isinstance(prov["localidades"], dict) and "localidad" in prov["localidades"]:
                localidades = prov["localidades"]["localidad"]
                if isinstance(localidades, dict):
                    return [localidades["__cdata"]]
                elif isinstance(localidades, list):
                    return [loc["__cdata"] for loc in localidades]
    return []

# 5️⃣ Provincia de un municipio dado
def provincia_por_municipio(provincias, nombre_municipio):
    for prov in provincias:
        if "localidades" in prov and isinstance(prov["localidades"], dict) and "localidad" in prov["localidades"]:
            localidades = prov["localidades"]["localidad"]
            if isinstance(localidades, dict):
                if localidades["__cdata"].lower() == nombre_municipio.lower():
                    return prov["nombre"]["__cdata"]
            elif isinstance(localidades, list):
                for loc in localidades:
                    if loc["__cdata"].lower() == nombre_municipio.lower():
                        return prov["nombre"]["__cdata"]
    return "Municipio no encontrado"

# 6️⃣ Provincias y municipios a partir de una lista de IDs
def provincias_por_ids(provincias, lista_ids):
    resultado = {}
    for prov in provincias:
        if prov["_id"] in lista_ids:
            if "localidades" in prov and isinstance(prov["localidades"], dict) and "localidad" in prov["localidades"]:
                localidades = prov["localidades"]["localidad"]
                if isinstance(localidades, dict):
                    resultado[prov["nombre"]["__cdata"]] = [localidades["__cdata"]]
                elif isinstance(localidades, list):
                    resultado[prov["nombre"]["__cdata"]] = [loc["__cdata"] for loc in localidades]
    return resultado

# 7️⃣ Número total de provincias y municipios
def total_provincias_municipios(provincias):
    total_prov = len(provincias)
    total_mun = sum(len(prov["localidades"]["localidad"]) if "localidades" in prov and isinstance(prov["localidades"]["localidad"], list) else (1 if "localidades" in prov else 0) for prov in provincias)
    return {"Total Provincias": total_prov, "Total Municipios": total_mun}

# 8️⃣ Provincias sin municipios
def provincias_sin_municipios(provincias):
    return [prov["nombre"]["__cdata"] for prov in provincias if "localidades" not in prov or not isinstance(prov["localidades"], dict) or "localidad" not in prov["localidades"]]

# 9️⃣ Municipios asociados a más de una provincia
def municipios_en_varias_provincias(provincias):
    municipios_dict = {}
    for prov in provincias:
        if "localidades" in prov and isinstance(prov["localidades"], dict) and "localidad" in prov["localidades"]:
            localidades = prov["localidades"]["localidad"]
            if isinstance(localidades, dict):
                municipio = localidades["__cdata"]
                municipios_dict.setdefault(municipio, []).append(prov["nombre"]["__cdata"])
            elif isinstance(localidades, list):
                for loc in localidades:
                    municipio = loc["__cdata"]
                    municipios_dict.setdefault(municipio, []).append(prov["nombre"]["__cdata"])
    
    return {mun: provs for mun, provs in municipios_dict.items() if len(provs) > 1}

# Cargar datos
provincias = cargar_datos()

# Pruebas de las funciones
print("Todas las provincias:", obtener_provincias(provincias))
print("Todos los municipios:", obtener_municipios(provincias)[:10])  # Mostramos solo 10 para no saturar
print("Provincias con total de municipios:", provincias_con_municipios(provincias))
print("Municipios de 'Alava':", municipios_por_provincia(provincias, "Alava"))
print("Provincia del municipio 'Vitoria-gasteiz':", provincia_por_municipio(provincias, "Vitoria-gasteiz"))
print("Provincias y municipios de IDs ['01', '02']:", provincias_por_ids(provincias, ['01', '02']))
print("Total de provincias y municipios:", total_provincias_municipios(provincias))
print("Provincias sin municipios:", provincias_sin_municipios(provincias))
print("Municipios en más de una provincia:", municipios_en_varias_provincias(provincias))
