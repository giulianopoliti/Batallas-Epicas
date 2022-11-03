import random

def comienzo():
    print()
    print("BATALLAS POKEMON".center(100))
    print()
    print("Batalla 1vs1 (1  ".rjust(50), end="")
    print("  2) Batalla 1vsPC".ljust(50))
    print()
    print("Como jugar (3  ".rjust(50), end="")
    print("  4) Salir".ljust(50))
    while True:
        try:
            entrada = int(input(">>>> ")) #agregar excepcion para cuando no se pone un numero -> ValueError
            assert entrada >= 1 and entrada <= 4
            return entrada
        except ValueError:
            print("Error. Ingresar 1, 2, 3 o 4.", end=" ")

def comoJugar():
    """printear todo el texto con las instrucciones de como jugar"""
    print("aca...")

    entrada = input("Enter para salir.")
    while entrada != "":
        print("Ingreso invalido.")
        entrada = input("Enter para salir.")
def personajes():
    personajes  = {
        "Charizard": ["Charizard", 250, 30, 35, 85, [1,16]],
        "Mario": ["Mario", 280, 25, 30, 70, [1,12]],
        "Tauros": ["Tauros", 225, 40,25,70, [1,12]],
        "Spiderman": ["Spiderman", 300, 20, 30, 50, [1,10]],
        "Harrypotter": ["HarryPotter", 180,45,40,100, [1,16]],
        "Goku": ["Goku", 210, 40,40,70, [1,12]],
        "Vegetta": ["Vegetta", 250, 32, 32, 80, [1,14]],
    }
    print("Personajes disponibles para elegir:")
    for personaje in personajes:
        print(personaje.center(10), end="")
    print()
    try:
        print("Quiere saber las estadisticas de todos los personajes?")
        decision = int(input("Ingrese 0 para verlas, cualquier caracter para continuar: "))
        assert decision == 0, "Valor inválido."
        columnas = len((personajes)["Goku"][:]) 
        filas = len((personajes).keys()) 
        matriz = [[0] * columnas for i in range(filas)]
        lista = ["PERSONAJES", "VIDA", "ATAQUE", "CURACION", "DEFINITIVA", "PROBABILIDAD DEFINITIVA"]
        listaProbabilidades = ["50%" , "75%", "75%", "80%", "50%", "75%", "57%" ]
        listapersonajes = list(personajes.keys())
        for i in range(filas):
            for j in range(columnas):
                matriz[0][j] = lista[j]
                matriz[i][0] = listapersonajes[i]
                datos = list(personajes.get(listapersonajes[i]))
                matriz[i][j] = datos[j]
                matriz[i][columnas-1] = listaProbabilidades[i]
        prolijidad = 0
        for i in range(filas):
            for j in range(columnas):
                print(str(matriz[i][j]).center(prolijidad+15), end="")
            print()
    except AssertionError:
        pass
    except ValueError:
        pass
    return personajes
def elegirPokemones(nombre, personajes):
    print()
    while True:
        try:
            print()
            ent = input(f"{nombre}, ingresar nombre del pokemon: ").capitalize()
            assert ent in personajes, "Pokemon no encontrado."

            print(f"Elegiste a {ent}! Estas son sus estadisticas:")
            print()
            print(f"Vida: {personajes[ent][1]}".center(25), end="")
            print(f"Ataque: {personajes[ent][2]}".center(25), end="")
            print(f"Curación: {personajes[ent][3]}".center(25), end="")
            print(f"Definitiva: {personajes[ent][4]}".center(25))
            print()

            seleccion = int(input("Ingresar 0 para confirmar eleccion o 1 para volver a elegir otro personaje: "))
            
            
            while seleccion <= 0 and seleccion >= 1:
                print("Numero invalido. Elegir una opcion correcta.")
                seleccion = int(input("Ingresar 0 para confirmar eleccion o 1 para volver a elegir otro personaje: "))

            else:
                if seleccion == 0:
                    return personajes[ent.capitalize()]
                    
                
            assert seleccion != 1, "Eleccion cancelada."

            # return personajes[ent.capitalize()]
            False
        except AssertionError as mensaje:
            print(mensaje)
        except ValueError:
            print("Ingresar solo 1 u 2.")

def habilidades():
    while True:
        try:
            print("Ingrese 2 para ataque comun, 3 para curacion, y 4 para la definitiva")
            decision = int(input("Que accion desea realizar?: "))

            assert 2 <= decision <= 4

            if decision == 2:
                return 2
            elif decision == 3:
                return 3
            elif decision == 4:
                return 4

        except AssertionError:
            print("Ingresar una opcion valida.")
        except ValueError:
            print("Ingresar una opcion valida.")
        
def jugadorVsJugador():
    nombreJugador1 = input("Ingresar nombre del jugador 1: ")
    pokemonJugador1 = elegirPokemones(nombreJugador1, personajes())
    nombreJugador2 = input("Ingresar nombre del jugador 2: ")
    pokemonJugador2 = elegirPokemones(nombreJugador2, personajes())

    return nombreJugador1, pokemonJugador1, nombreJugador2, pokemonJugador2

def partida(jugador1, personaje1, jugador2, personaje2):
    
    turno = 0
    print()

    print(jugador1.ljust(40), end="")
    print("JUGADORES".center(20), end="")
    print(jugador2.rjust(40))

    print(str(personaje1[0]).ljust(40), end="")
    print("PERSONAJE".center(20), end="")
    print(str(personaje2[0]).rjust(40))

    print()

    print(str(personaje1[1]).ljust(40), end="")
    print("VIDA".center(20), end="")
    print(str(personaje2[1]).rjust(40))
    
    print(str(personaje1[2]).ljust(40), end="")
    print("ATAQUE".center(20), end="")
    print(str(personaje2[2]).rjust(40))

    print(str(personaje1[3]).ljust(40), end="")
    print("CURACION".center(20), end="")
    print(str(personaje2[3]).rjust(40))

    print(str(personaje1[4]).ljust(40), end="")
    print("ULTI".center(20), end="")
    print(str(personaje2[4]).rjust(40))

    vidaPersonaje1 = personaje1[1]
    vidaPersonaje2 = personaje2[1]

    # [tipo, vida, ataque, curacion, ulti]
    contador1 = 0
    contador2 = 0
    while vidaPersonaje1 > 0 and vidaPersonaje2 > 0:
        print()
        if turno == 0:
            print(f"Turno de {jugador1}:")
            accion = habilidades()
            contador1 += 1
            while accion == 4 and contador1 < 3:
                print("La definitiva la tiene cada 3 turnos y aun no esta disponible, ingrese otra habilidad.")
                accion = habilidades()
            if accion == 3: #se suma la vida xq se cura
                vidaPersonaje1 += personaje1[accion]
            elif accion == 4:
                if random.randint(personaje1[5][0], personaje1 [5][1]) <= 8:
                    vidaPersonaje2 -= personaje1[accion]
                    contador1 = 0
                else:
                    contador1 = 3
                    print("Has fallado la definitiva. Pierdes el turno.")
                    
            else: #ataca
                vidaPersonaje2 -= personaje1[accion]

            turno = 1

            print(str(vidaPersonaje1).ljust(50), end="")
            print(str(vidaPersonaje2).rjust(50))

        else:
            print(f"Turno de {jugador2}:")
            accion = habilidades()
            contador2 += 1
            while accion == 4 and contador2 < 3:
                print("La definitiva la tiene cada 3 turnos y aun no esta disponible, ingrese otra habilidad.")
                accion = habilidades()
            
            if accion == 3:
                vidaPersonaje2 += personaje2[accion]
            elif accion == 4:
                if random.randint(personaje2[5][0], personaje2[5][1]) <= 8:
                    vidaPersonaje1 -= personaje2[accion]
                    contador2 = 0
                else:
                    print("Has fallado la definitiva. Pierdes el turno")
                    contador2 = 3
            else:
                vidaPersonaje1 -= personaje2[accion]

            turno = 0

            print(str(vidaPersonaje1).ljust(50), end="")
            print(str(vidaPersonaje2).rjust(50))
        
    if vidaPersonaje1 > 0:
        ganador = jugador1
        print(f"{jugador1} con {personaje1[0]}, gano!".center(100))
        print(f"{jugador2} con {pokemon2[0]}, perdio.".center(100))
    else:
        ganador = jugador2
        print(f"{jugador2} con {pokemon2[0]}, gano!".center(100))
        print(f"{jugador1} con {personaje1[0]}, perdio.".center(100))

    return ganador

def jugadorVsPc():
    pass

jugar = 0
modoDeJuego = comienzo()
if modoDeJuego == 1:
    while jugar == 0:
        nombre1, pokemon1, nombre2, pokemon2 = jugadorVsJugador()
        ganador = partida(nombre1, pokemon1, nombre2, pokemon2)

        jugar = int(input("Jugar de nuevo? (0 para continuar, cualquier caracter para salir): "))
    else:
        print("Gracias por jugar!")

elif modoDeJuego == 2:
    jugadorVsPc()

elif modoDeJuego == 3:
    comoJugar()

else:
    print("Hasta la proxima!") 
