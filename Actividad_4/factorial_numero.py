num = int(input("Número para calcular factorial: "))
factorial = 1
if num < 0:
    print("Error: El número debe ser no negativo.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es:", factorial)