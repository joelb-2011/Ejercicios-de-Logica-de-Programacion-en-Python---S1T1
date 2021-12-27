#Ejercicio 11: Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades, decenas, centenas y unidades de mil.

numero = int(input("Ingrese un número de 4 dígitos: "))
unimil = (numero-(numero%1000))/1000
mil = numero%1000
cen = (mil-(mil%100))/100
cien = numero%100
dec = (cien-(cien%10))/10
uni = cien%10
print("Unidad de mil:", int(unimil))
print("Centena:", int(cen))
print("Decena:", int(dec))
print("Unidad:", int(uni))
