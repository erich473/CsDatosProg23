"""Introducir los lados de un triángulo y visualizar por pantalla si dicho
triángulo es equilátero, isósceles o escaleno."""

print( "A continuación coloque las medidas del triangulo a verificar: ")

A = int(input("Lado A: "))
B = int(input("Lado B: "))
C = int(input("Lado C: "))

if A == B and A == C:
    print("Triangulo EQUILATERO")
elif A != B and A != C:
    print("Triangulo ESCALENO")
else:
    print("Triangulo ISOSCELES")

print("Fin de operacion")
