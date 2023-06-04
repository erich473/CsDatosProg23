""" Realice un programa que lea tres números, muestre cuál es el mayor y
determine si es par o impar."""

num_1 = int(input("Coloque numero 1: "))
num_2 = int(input("Coloque numero 2: "))
num_3 = int(input("Coloque numero 3: "))

if num_1 == num_2 == num_3:
    print("Los numeros son iguales")
elif num_1 > (num_2 and num_3):
    print(f"El numero mayor es: {num_1}")
elif num_2 > (num_1 and num_3):
    print(f"El numero mayor es {num_2}")
else:
    print(f"El numero mayor es: {num_3}")
    


if num_1 % 2 == 0:
    print("El numero 1 Es numero PAR")
else:
    print("El numero 1 Es numero IMPAR")

if num_2 % 2 == 0:
    print("El numero 2 Es numero PAR")
else:
    print("El numero 2 Es numero IMPAR")

if num_3 % 2 == 0:
    print("El numero 3 Es numero PAR")
else:
    print("El numero 3 Es numero IMPAR")

print("FIN")
