""" Leer 15 números negativos y convertirlos a positivos e imprimir dichos
números. """

#Trabajo con for:

"""n_negativos = []
n_positivos = None

for i in range (1, 16):
    n = int(input(f"Colocar numeros negativos para convertirlos a positivos {i}: "))
    if n < 0:
        n_negativos.append(-n) 
    else:
        n_positivos=None

print("Numeros convertidos: ", n_negativos)"""

#Trabajo con wile:

n_negativos = []
n_positivos = None
x = 1
while x <=15:
    n = int(input(f"Colocar numero negativo para convertir a positivo {x}: "))
    if n < 0:
        n_negativos.append(-n)
    else:
        n_positivos=None
    x += 1
print("Numeros convertidos: ", n_negativos)