import random

# Clases
class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.vida_max = random.randint(150, 400)
        self.vida_actual = self.vida_max

entrenador1 = None
pokemon1 = None
entrenador2 = None
pokemon2 = None
ganadas = 0
perdidas = 0

# Funciones
def crearEntrenadorPokemon(n):
    global entrenador1, pokemon1, entrenador2, pokemon2

    if n == 1:
        nombre_ent = input("Ingrese nombre de entrenador: ")
        nombre_pok = input("Ingrese el nombre de su pokemon: ")
        entrenador1 = Entrenador(nombre_ent)
        pokemon1 = Pokemon(nombre_pok)
        print("\n-- Su pokemon ha sido creado con éxito:")
        print("Entrenador:", entrenador1.nombre)
        print("Pokemon:", pokemon1.nombre)
        print("Ataque máximo:", pokemon1.max_ataque)
        print("Vida máxima:", pokemon1.vida_max)
        print("Vida actual:", pokemon1.vida_actual)
    else:
        nombre_ent = input("\nIngrese nombre del entrenador rival: ")
        nombre_pok = input("Ingrese nombre del pokemon rival: ")
        entrenador2 = Entrenador(nombre_ent)
        pokemon2 = Pokemon(nombre_pok)
        print("\n-- El pokemon rival ha sido creado:")
        print("Entrenador:", entrenador2.nombre)
        print("Pokemon:", pokemon2.nombre)
        print("Ataque máximo:", pokemon2.max_ataque)
        print("Vida máxima:", pokemon2.vida_max)
        print("Vida actual:", pokemon2.vida_actual)


def valorDeAtaque(n):
    if n == 1:
        return random.randint(0, pokemon1.max_ataque)
    else:
        return random.randint(0, pokemon2.max_ataque)


def defender(n, valorAtaque):
    defensa = random.randint(1, 6)
    if defensa == 6:
        print("--- ¡El ataque fue bloqueado con una defensa de 6!")
        valorAtaque = 0

    if n == 1:
        pokemon1.vida_actual -= valorAtaque
        if pokemon1.vida_actual < 0:
            pokemon1.vida_actual = 0
        return pokemon1.vida_actual
    else:
        pokemon2.vida_actual -= valorAtaque
        if pokemon2.vida_actual < 0:
            pokemon2.vida_actual = 0
        return pokemon2.vida_actual


def recuperar():
    pokemon1.vida_actual = pokemon1.vida_max


def main():
    global ganadas, perdidas

    print("=== BIENVENIDO A LA BATALLA POKEMON ===")
    crearEntrenadorPokemon(1)  

    while True:
        print("\n¿Qué desea hacer?")
        print("P - Pelear")
        print("F - Finalizar")
        opcion = input("Elija opción: ").upper()

        if opcion == "F":
            print("\n=== FIN DEL JUEGO ===")
            print("Entrenador:", entrenador1.nombre)
            print("Pokemon:", pokemon1.nombre)
            print("Ataque máximo:", pokemon1.max_ataque)
            print("Vida máxima:", pokemon1.vida_max)
            print("Encuentros ganados:", ganadas)
            print("Encuentros perdidos:", perdidas)
            break

        elif opcion == "P":
            recuperar()
            crearEntrenadorPokemon(2) 

            print("\n=== INICIA LA PELEA ===")
            turno = 1  

            while pokemon1.vida_actual > 0 and pokemon2.vida_actual > 0:
                if turno == 1:
                    print("\n-- Su turno de atacar")
                    ataque = valorDeAtaque(1)
                    print("Su pokemon atacó con:", ataque)
                    vida = defender(2, ataque)
                    print("Vida actual del pokemon rival:", vida)
                    turno = 2
                else:
                    print("\n-- Turno del rival")
                    ataque = valorDeAtaque(2)
                    print("El pokemon rival atacó con:", ataque)
                    vida = defender(1, ataque)
                    print("Vida actual de su pokemon:", vida)
                    turno = 1

            if pokemon1.vida_actual > 0:
                print("\n--- Usted ha ganado la pelea!")
                print("Ganador:", entrenador1.nombre, "-", pokemon1.nombre)
                ganadas += 1
            else:
                print("\n--- Usted ha perdido la pelea...")
                print("Ganador:", entrenador2.nombre, "-", pokemon2.nombre)
                perdidas += 1
        else:
            print("Opción no válida, intente otra vez.")

main()
