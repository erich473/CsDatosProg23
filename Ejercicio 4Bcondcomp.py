"""Confeccione un programa que pida un número del 1 al 7 y diga el día de
la semana correspondiente."""

print("Coloque un numero del 1 al 7")

numero = int(input("Numero: "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miercoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sabado")
elif numero == 7:
    print("Domingo")
else:
    print("Numero incorrecto")

print("Fin") 

