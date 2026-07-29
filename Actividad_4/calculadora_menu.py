while True:
    print("1. Suma 2. Resta 3. Multiplicación 4. División 5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 5:
        break
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    match opcion:
        case 1:
            print(a + b)
        case 2:
            print(a - b)
        case 3:
            print(a * b)
        case 4:
            if b != 0:
                print(a / b)
            else:
                print("Error: No se puede dividir entre cero.")
    respuesta = input("¿Desea realizar otra operación? (s/n): ").lower()  
    if respuesta != "s":
        break
        