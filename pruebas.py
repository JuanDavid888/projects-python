print("¡Bienvenido Usuario!")

nameUsuario = input("Ingrese su nombre: ")

print(f"Hola {nameUsuario}")

print("Dime un número y te diré algo sobre él")

numberUsuario = int(input())

if numberUsuario % 2 == 0:
    print(f"el número {numberUsuario} que ingresaste es par")

else:
    print(f"el número {numberUsuario} que ingresaste es impar")

