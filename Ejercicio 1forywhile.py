#Programa que lee 4 numeros y dice cuantos son pares y cuantos impares.
#Devuelve la suma de los pares

par = impar = 0 
suma_numerospares = 0

for i in range (4):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        par += 1
        suma_numerospares += num
    else:
        impar +=1
print("Hay", par, "numeros pares y", impar, "numeros impares")
print("La suma de los numeros pares es: ", suma_numerospares)

