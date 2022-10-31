import random

def comienzo():
    print()
    print("BATALLAS POKEMON".center(100))
    print()
    print("Batalla 1vs1 (1 ".rjust(50), end="")
    print(" 2) Batalla 1vsPC".ljust(20))
    while True:
        try:
            entrada = int(input(">>>> ")) #agregar excepcion para cuando no se pone un numero -> ValueError
            assert entrada == 1 or entrada == 2
            return entrada
            break
        except ValueError:
            print("Error. Ingresar 1 u 2.", end=" ")


             #se retorna lo q entro el usuario para pasarlo como parametro en la proxima funcion

def  elegirPokemones(nombre):
    pokemones  = {
        "Charizard" : [ "fuego" , 250, 30, 35, 70],
        "Sandlash" : [ "tierra" , 280, 25, 30, 60 ],
        "Tauros" : [ "normal" , 225, 40,25,80],
        "Dewgong" : [ "agua" , 300, 20, 30, 50],
        "Harrypotter" : ["mago", 180,45,40,90],
        "Goku" : ["luchador", 210, 40,40,70],
        "Vegetta" : ["luchador", 250, 32, 32, 70]
    }
    for pokemon, datos in pokemones.items():
        print ("El personaje", pokemon, "es un", datos[0], "su vida es", datos [1], "y su ataque", datos [2])
    while True:
        try:
            ent = input(f"{nombre}, ingresar nombre del pokemon: ")
            assert ent.capitalize() in pokemones
            return pokemones[ent.capitalize()]
            False
        except AssertionError:
            print(print("Pokemon no encontrado."))
def habilidades():
    print ("Ingrese 2 para ataque comun, 3 para curacion, y 3 para la definitiva")
    decision = int(input("Que accion desea realizar?: "))
    if decision == 2:
        return 2
    elif decision == 3:
        return 3
    elif decision == 4:
        return 4
    else:
        habilidades()
        
def jugadorVsJugador():
    nombreJugador1 = input("Ingresar nombre del jugador 1: ")
    pokemonJugador1 = elegirPokemones(nombreJugador1)
    nombreJugador2 = input("Ingresar nombre del jugador 2: ")
    pokemonJugador2 = elegirPokemones(nombreJugador2)

    return nombreJugador1, pokemonJugador1, nombreJugador2, pokemonJugador2

def partida(jugador1, pokemon1, jugador2, pokemon2):
    turno = 0
    print("Elegiste a", pokemon1, "su vida es", pokemon1[1], "su ataque basico", pokemon1[2], "su curacion es", pokemon1[3], "y su definitiva", pokemon1[4])
    print("Elegiste a", pokemon2, "su vida es", pokemon2[1], "su ataque basico", pokemon2[2], "su curacion es", pokemon2[3], "y su definitiva", pokemon2[4])
    vidaPokemon1 = pokemon1[1]
    vidaPokemon2 = pokemon2[1]


    while vidaPokemon1 > 0 and vidaPokemon2 > 0:
        print()
        if turno == 0:
            vidaPokemon2 -= pokemon1[habilidades()]
            turno = 1
            print(vidaPokemon2)

        else:
            vidaPokemon1 -= pokemon2[habilidades()]
            turno = 0
            print(vidaPokemon1)

        

def jugadorVsPc():
    pass

modoDeJuego = comienzo()
if modoDeJuego == 1:
    nombre1, pokemon1, nombre2, pokemon2 = jugadorVsJugador()
    partida(nombre1, pokemon1, nombre2, pokemon2)
else:
    jugadorVsPc()
