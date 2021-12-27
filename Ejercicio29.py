#Ejercicio 29: Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla del 1 hasta la del 10.

inicio = 1
fin = 10

for factor in range(inicio, fin + 1):  
    for f in range(inicio, fin + 1):
	    print(f"{factor} x {f} =  {factor * f}")