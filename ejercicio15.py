#Ejercicio 15: Para un valor entero positivo que representa una cantidad en segundos, indicar su equivalente en minutos, horas y días.

segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos // 3600
minutos = segundos // 60
dias = segundos // 86400

print("Días: " + str(dias))
print("Horas: " + str(horas))
print("Minutos: " + str(minutos))