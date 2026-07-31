#Calculadora de nota final con division de rango
calificacion = float(input("Nota parciales (0-100): "))
proyecto = float(input("Nota proyecto (0-100): "))
examen = float(input("Nota examen final (0-100): "))
if calificacion < 0 or calificacion > 100 or proyecto < 0 or proyecto > 100 or examen < 0 or examen > 100:
    print("Error: Las notas deben estar entre 0 y 100.")
else:
    nota_final = (calificacion * 0.4) + (proyecto * 0.3) + (examen * 0.3)
    print(f"La nota final es: {nota_final}")