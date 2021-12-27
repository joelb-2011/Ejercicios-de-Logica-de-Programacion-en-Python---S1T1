#Ejercicio 16: Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el mayor? y ¿cuál es el segundo mayor?

numeroa = int(input("Ingrese un número A: "))
numerob = int(input("Ingrese un número B: "))
numeroc = int(input("Ingrese un número C: "))

if numeroa > numerob and numeroa > numeroc:
    print("El primer número mayor es A con: " + str(numeroa))
elif numerob > numeroa and numerob > numeroc:
    print("El primer número mayor es B con: " + str(numerob))
elif numeroc > numeroa and numeroc > numerob:
    print("El primer número mayor es C con: " + str(numeroc))

if (numeroa < numerob and numeroa > numeroc) or (numeroa > numerob and numeroa < numeroc):
    print("El segundo número mayor es A con: " + str(numeroa))
elif (numerob < numeroa and numerob > numeroc) or (numerob > numeroa and numerob < numeroc):
    print("El segundo número mayor es B con: " + str(numerob))
elif (numeroc < numeroa and numeroc > numerob) or (numeroc > numeroa and numeroc < numerob):
    print("El segundo número mayor es B con: " + str(numeroc))