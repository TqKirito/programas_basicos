suma = 0 
contador = 0

while True:
    num = float(input("Ingrese un número positivo (o un número negativo para terminar): "))
    if num < 0:
        break
    if num > 0:
        suma += num
        contador += 1

if contador > 0:
    media = suma / contador
    print("La media de los números es:", media)
else:
    print("No se ingresaron números positivos.")