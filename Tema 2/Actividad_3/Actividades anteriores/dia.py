#Match: evaluar una variable y compara con diferentes casos hasta que coincida con alguno de ellos
dia = int(input("Ingrese un número del 1 al 7 para indicar el día de la semana: ") )
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número no válido")