""" Realice un programa que pida un número del 1 al 12 y diga el nombre
del mes correspondiente. """

print("Coloque un numero del 1 al 12 para saber el mes correspondiente")

n = int(input("Numero: "))

if n == 1:
    print("Enero")
elif n == 2:
    print("Febrero")
elif n == 3:
    print("Marzo")
elif n == 4:
    print("Abril")
elif n == 5:
    print("Mayo")
elif n == 6:
    print("Junio")
elif n == 7:
    print("Julio")
elif n == 8:
    print("Agosto")
elif n == 9:
    print("Septiembre")
elif n == 10:
    print("Octubre")
elif n == 11:
    print("Noviembre")
elif n == 12:
    print("Diciembre")
else:
    print("Numero incorrecto")

print("Fin")