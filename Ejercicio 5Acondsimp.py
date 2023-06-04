"""Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
de cambio quiere, si de dólares a pesos o viceversa."""

# Inicio
"""pesos_dolares = int(input("Ingresar pesos: "))
dolar = 450

print("Son u$$: ", pesos_dolares / dolar)"""


# Mejora


"""pesos_dolares = int(input("Ingresar pesos: "))
dolar = 450


print("Son u$$: ", pesos_dolares / dolar)


dolares_pesos = int(input("Ingresar dolares: "))
peso = 450

print("Son $: ", dolares_pesos * peso)"""

print(" Sistema integral para convertir pesos a dolares y viseversa")

eleccion = input("Elija una opcion: 'pesos_dolares': A - 'dolares_pesos': B: ")

#pesos_dolares = int("Ingresar pesos: ")
dolar = 450
peso = 450

if eleccion == "A":
    print(int(input("Ingresar pesos: ")) / dolar)
    print("Total de DOLARES u$$")

if eleccion == "B":
    print(int(input("Ingresar dolares: ")) * peso)
    print("Total de PESOS $")

print("Muchas gracias por utilizar nuestro sistema!")