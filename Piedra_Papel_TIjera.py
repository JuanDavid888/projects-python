print("Bienvenido al juego")

nameUsuario = input("Dime tu nombre: ")

import random
def elegir_opciones(opciones):
    return random.choice(opciones)

opciones = ["piedra", "papel", "tijera"]

piedra = (">tijera") and ("<papel")
tijera = (">papel") and ("<piedra")
papel = (">piedra") and ("<tijera")

usuario = input("Escoge entre papel, piedra o tijera: ").lower()


if usuario not in opciones:
    input("Escoge otra vez: ")

else:
    maquina = random.choice(opciones)
    print(f"La PC escogió {maquina}")

if usuario == maquina:
    print(f"Fue un empate {nameUsuario}")

elif (usuario == papel and maquina == piedra) or (usuario == piedra and maquina == tijera) or (usuario == tijera and maquina == papel):
    print(f"¡Felicidades, ganaste {nameUsuario}!")
else:
    print(f"Tal vez la próxima ganes {nameUsuario}")

