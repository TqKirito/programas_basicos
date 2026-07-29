nota =float (input("Ingrese su calificación: (0-100) "))
if nota < 0 or nota > 100:
    print("Error: La calificación debe estar entre 0 y 100.")
else:
    if nota >= 90:
        letra = "A"

    elif nota >= 80:
        letra = "B"

    elif nota >= 70:
        letra = "C"

    elif nota >= 60:
        letra = "D"

    else:
        letra = "F"

    print("La calificación es:", letra)