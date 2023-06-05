""" Leer 10 números y mostrar solamente los números positivos, y su
sumatoria. """

n_negativo = 0
n_positivo = 0
suma_positivos = 0

for i in range (1, 11):
    n = int(input("Colocar numero: " + str(i)+ " "))
    if n > 0:
        n_positivo += 1
        suma_positivos += n
    else:
        n_negativo += 1

        
        
print("Numeros positvivos: ", n_positivo)
print("La suma de los numeros positivos es: ", suma_positivos)

    
    