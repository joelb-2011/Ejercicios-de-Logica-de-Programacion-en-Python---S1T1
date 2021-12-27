#Ejercicio 6: Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.

from math import sqrt

lado1 = float(input("Ingrese en centímetros el lado 1: "))
lado2 = float(input("Ingrese en centímetros el lado 2: "))

hipotenusa = sqrt(lado1**2 + lado2**2)

print("El resultado de la hipotenusa es: {}".format(hipotenusa))