#Programa que lee 10 numeros y obtiene la cantidad de mayores y menores a 100.
#Identifica cual es el minimo y cual es el maximo
menores = 0
mayores = 0
minimo = None
maximo = None

for i in range(10):
    num = int(input("Ingrese un numero: "))
    if num > 100:
        mayores += 1
    else:
        menores += 1

    if maximo is None or num > maximo:
        maximo = num

    if minimo is None or num < minimo:
        minimo = num    

print("Cantidad de numeros mayores a 100: ", mayores)
print("Cantidad de numeros menores a 100: ", menores)
print("Numero maximo: ",maximo)
print("Numero minimo: ",minimo)