import math
def mcd(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = mcd(num1, num2)
resultado_math = math.gcd(num1, num2)
print(f"El MCD de {num1} y {num2} es: {resultado}")
print(f"El MCD usando math.gcd de {num1} y {num2} es: {resultado_math}")
print("Los resultados son iguales." if resultado == resultado_math else "No coinciden")

if num1 == 0 and num2 == 0:
    print("Caso especial: ambos números siendo cero.")
else:
    print("Programa terminado correctamente.")