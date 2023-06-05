""" Ingresar las edades y el sexo de 15 personas y determinar cuántas son
mujeres, cuántos varones, cuántos mayores de edad y cuántos
menores de edad. """


mayores = 0
menores = 0
varones = 0
mujeres = 0

for i in range (1, 15):
    edad = int(input("Ingrese la edad de la persona:" + str(i) + " "))
    sexo = input("Ingrese el sexo de la persona: " + str(i)  + " (m/v): ")

    if edad > 18:
        mayores += 1
    else:
        menores += 1
    if sexo.lower() == "m":
        mujeres += 1
    else:
        varones += 1


print("Cantidad de mayores de edad: ", mayores)
print("Cantidad de menores de edad: ", menores)
print("Sexo femenino: ", mujeres)
print("Sexo masculino: ", varones) 
