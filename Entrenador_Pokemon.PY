
print("Soy el Profesor Oak")
genero= input("¿Eres un chico o una chica? " ).lower()
edad= input ("¿Qué edad tienes? ")
if genero=="chico" and edad >= "10":
    print("Bienvenido al mundo Pokemon!")
elif genero=="chica" and edad >= "10":
    print("Bienvenida al mundo Pokemon!")
else:
    print("No tienes edad para entrenar Pokemones")
    exit() # Se termina el programa si no tiene la edad determinada
region= input("Necesitas un compañero de viaje, ¿en qué región te encuentas?: ").lower()
# Asignación del compañero basado en la región y el género
if region== "kanto" and genero== "chico":
    print("Tu compañera es Misty")
elif region== "kanto" and genero== "chica":
    print("Tu compañero es Brock")
elif region== "johto" and genero== "chico":
    print("Tu compañera es Cris")
elif region== "johto" and genero== "chica":
    print("Tu compañero es Eco")
elif region== "hoenn" and genero== "chico":
     print("Tu compañera es Aura")
elif region== "hoenn" and genero== "chica": 
    print("Tu compañero es Bruno")
elif region== "sinnoh" and genero== "chico":
     print("Tu compañera es Hoja")
elif region== "sinnoh" and genero== "chica":
    print("Tu compañero es Rojo")
elif region== "teselia" and genero== "chico":
     print("Tu compañera es Maya")
elif region== "teselia" and genero== "chica":
    print("Tu compañero es León")
elif region== "kalos" and genero== "chico":
     print("Tu compañera es Lira")
elif region== "kalos" and genero== "chica":
    print("Tu compañero es Eco")
elif region== "alola" and genero== "chico":
     print("Tu compañera es Nanci")
elif region== "alola" and genero== "chica":
    print("Tu compañero es Rizzo")
elif region== "galar" and genero== "chico":
     print("Tu compañera es Gloria")
elif region== "galar" and genero== "chica":
    print("Tu compañero es Victor")
elif region== "paldea" and genero== "chico":
     print("Tu compañera es Juliana")
elif region== "paldea" and genero== "chica":
    print("Tu compañero es Florian")
else:
    print("ingresa una región válida")
    exit() # Termina el programa si no se coloca una región válida

# Selección de Pokemón inicial
tipo_de_pokemon= input("¿Qué tipo de Pokemón deseas? Elige entre agua, fuego y planta: ").lower()

# Diccionario de Pokémon iniciales por región y tipo
pokemon_iniciales = {
    "kanto": {"agua": "Squirtle", "fuego": "Charmander", "planta": "Bulbasaur"},
    "johto": {"agua": "Totodile", "fuego": "Cyndaquil", "planta": "Chikorita"},
    "hoenn": {"agua": "Mudkip", "fuego": "Torchic", "planta": "Treecko"},
    "sinnoh": {"agua": "Piplup", "fuego": "Chimchar", "planta": "Turtwig"},
    "teselia": {"agua": "Oshawott", "fuego": "Blaziken", "planta": "Snivy"},
    "kalos": {"agua": "Frogadier", "fuego": "Fennekin", "planta": "Chespin"},
    "alola": {"agua": "Popplio", "fuego": "Litten", "planta": "Rowlet"},
    "galar": {"agua": "Sobble", "fuego": "Scorbunny", "planta": "Grookey"},
    "paldea": {"agua": "Quaxly", "fuego": "Fuecoco", "planta": "Sprigatito"}
}

# Determinar el Pokémon inicial basado en la región y tipo
if region in pokemon_iniciales and tipo_de_pokemon in pokemon_iniciales[region]:
    pokemon = pokemon_iniciales[region][tipo_de_pokemon]
    print(f"Tu Pokémon inicial es: {pokemon}")
else:
    print("Ingresa un tipo de Pokémon válido")
    exit() # Se cierra el programa 