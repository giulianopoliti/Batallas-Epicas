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

def elegirPokemones(nombre):
    pokemones = {
        "Charizard": ["fuego", 120, 30],
        "Sandlash": ["tierra", 95, 25],
        "Tauros": ["normal", 110, 30],
        "Dewgong": ["agua", 90, 25]
    }
    while True:
        try:
            ent = input(f"{nombre}, ingresar nombre del pokemon: ")
            assert ent.capitalize() in pokemones
            return pokemones[ent.capitalize()]
            False
        except AssertionError:
            print(print("Pokemon no encontrado."))

def jugadorVsJugador():
    nombreJugador1 = input("Ingresar nombre del jugador 1: ")
    pokemonJugador1 = elegirPokemones(nombreJugador1)
    nombreJugador2 = input("Ingresar nombre del jugador 2: ")
    pokemonJugador2 = elegirPokemones(nombreJugador2)

    return nombreJugador1, pokemonJugador1, nombreJugador2, pokemonJugador2

def partida(jugador1, jugador2, pokemon1, pokemon2):
    turno = 0

    vidaPokemon1 = pokemon1[1]
    vidaPokemon2 = pokemon2[1]

    ataquePokemon1 = pokemon1[2]
    ataquePokemon2 = pokemon2[2]


    while vidaPokemon1 > 0 and vidaPokemon2 > 0:
        print()
        if turno == 0:
            vidaPokemon2 -= ataquePokemon1
            turno = 1
            print(vidaPokemon2)

        else:
            vidaPokemon1 -= ataquePokemon2
            turno = 0
            print(vidaPokemon1)

        

def jugadorVsPc():
    pass

modoDeJuego = comienzo()
if modoDeJuego == 1:
    nombre1, pokemon1, nombre2, pokemon2 = jugadorVsJugador()
    partida(nombre1, nombre2, pokemon1, pokemon2)
else:
    jugadorVsPc()