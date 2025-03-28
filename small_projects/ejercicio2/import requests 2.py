import requests

API_KEY = "c4b062387f14722bcffa482f46d5f54c"  # Reemplaza con tu clave de API de OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obtener_clima(ciudad):
    if not ciudad.strip():
        print("El nombre de la ciudad no puede estar vacío. Inténtalo de nuevo.")
        return

    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        datos = response.json()
        descripcion = datos["weather"][0]["description"]
        temperatura = datos["main"]["temp"]
        print(f"El clima en {ciudad} es: {descripcion}")
        print(f"Temperatura: {temperatura} grados Celsius")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    except KeyError:
        print("Error al procesar los datos de la respuesta. Verifica el nombre de la ciudad.")

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        ciudad = input("Introduce el nombre de la ciudad (o escribe 'salir' para terminar): ")
        if ciudad.lower() == "salir":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        obtener_clima(ciudad)