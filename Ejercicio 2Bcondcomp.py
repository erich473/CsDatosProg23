""" Realice un programa que le permita al usuario simular el pago
ingresando el importe y la forma de pago:
• Contado (1): se aplica un descuento del 10% al importe
• Tarjeta (2): se aplica un interés de 10%
• Débito (3): se aplica un descuento del 5% """

"""print("Simulacion de pago - A continuacion Ingrese los datos necesarios: ")

A = int(input("Pago Contado (1): "))
B = int(input("Pago con Tarjeta (2): "))
C = int(input("Pago con Debito (3): "))

if A :
  print("Se aplico descuento del 10%. Abona un total de: ", A - A * 10/100)

if B :
  print("Se aplico recargo del 10%. Abona un total de: ", B + B * 10/100)

if C :
  print("Se aplico un descuento del 5%. Abona un total de: ", C - C * 5/100)

print("Fin operacion") """
 
 # Mejora con eleccion  de OPCIONES:

print("Elija su opcion: (A) 'Pago Contado', (B) 'Pago Tarjeta', (C) 'Pago Debito': ")

opcion = input("Coloque una opcion: ")

if opcion == "A":
    print("Pago Contado")

    A = float(input("Importe:$ "))

    if A :
        print("Descuento del 10%:$ ",A * 10/100)
        print("Se aplica un descuento del 10%. Abona un total de:$ ", A - A * 10/100 )

if opcion == "B":
    print("Pago Tarjeta")

    B = float(input("Importe:$ "))

    if B :
        print("Recargo del 10%:$ ",B * 10/100)
        print("Se aplica un recargo del 10%. Abona un total de: ", B + B * 10/100 )

if opcion == "C":
    print("Pago con Debito")

    C = float(input("$: "))

    if C :
        print("Descuento del 5%:$ ",C * 5/100)
        print("Se aplica un descuento del 5%. Abona un total de: ", C - C * 5/100 )


print("Final del proceso")


    









