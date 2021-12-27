#Ejercicio 22: Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene dicho número.

numero = int(input("Ingrese cualquier número: "))
contador = len(str(numero))

print("Usted ha ingresado", contador,"dígitos.")