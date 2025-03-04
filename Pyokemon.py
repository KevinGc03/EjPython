import requests

# Función para obtener información del Pokémon desde PokeAPI
def obtener_datos_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return {
            "Nombre": datos["name"],
            "ID": datos["id"],
            "Altura": datos["height"],
            "Peso": datos["weight"],
            "Tipos": [tipo["type"]["name"] for tipo in datos["types"]]
        }
    else:
        return {"error": "Pokémon no encontrado"}

# Solicitar al usuario el nombre del Pokémon
nombre_pokemon = input("Introduce el nombre del Pokémon: ")
informacion = obtener_datos_pokemon(nombre_pokemon)

# Mostrar información
if "error" in informacion:
    print(informacion["error"])
else:
    print(f"Nombre: {informacion['Nombre']}")
    print(f"ID: {informacion['ID']}")
    print(f"Altura: {informacion['Altura']}")
    print(f"Peso: {informacion['Peso']}")
    print(f"Tipos: {', '.join(informacion['Tipos'])}")
