opcion = ""
while opcion != "salir":
    print("\n--- Menú ---")
    print("1. Saludar")
    print("2. Despedir")
    print('Escriba "salir" para terminar')
    opcion = input("Opción: ")
    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        print("Adiós.")
    elif opcion != "salir":
        print("Opción no válida.")