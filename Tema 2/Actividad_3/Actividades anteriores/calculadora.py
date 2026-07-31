opcion = input("Ingrese la operacion a realizar (suma, resta, multiplicacion, division): ")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
match opcion:
    case "suma":    
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")   
    case "resta":
        resultado = num1 - num2 
        print(f"El resultado de la resta es: {resultado}")
    case "multiplicacion":
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    case "division":
        if num2 != 0:
            print(f"Error matematico")
        else:
            resultado = num1/num2
        print (f"El resultado de la division es: {resultado}")