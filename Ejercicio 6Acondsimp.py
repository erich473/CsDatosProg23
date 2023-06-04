"""Realice un programa donde el usuario ingrese su edad. Si es mayor de
16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”."""

print(" Sistema para validacion de votantes de acuerdo a su edad.")
edad = int(input("Coloque su edad: "))

if edad > 16:
    print("'Puede votar'")
    print("Suerte con su eleccion!")

else:
    print("'No vota'")
    print("Vuelva cuando tenga la edad apropiada.")

print("Muchas gracias!")

