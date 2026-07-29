mes = int(input("Número del mes (1-12): "))
match mes:
    case 1 | 2 | 12: 
        estacion = "Invierno"
    case 3 | 4 | 5:
        estacion = "Primavera"
    case 6 | 7 | 8:
        estacion = "Verano"
    case 9 | 10 | 11:
        estacion = "Otoño"
    case _:
        estacion = None
        estacion = "Mes inválido"
print("Estación del año:", estacion)