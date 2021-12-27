#Ejercicio 13: Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es capicúa.

n = int(input("Ingrese un número: "))
if n > 9999 and n < 100000:
    a = n // 10000
    b = n % 10
    if a == b:
        print("El número",n,"es un número capicúa.")
    else:
        print("El número",n,"no es un número capicúa.")
else:
    print("Ingrese un número de 5 dígitos.")