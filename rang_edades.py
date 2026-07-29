edad = int(input("Ingrese su edad: "))
if edad == 0:
    print("Edad recien nacida")
elif edad < 13 and edad > 0:
    print("Niño")
elif edad < 18 and edad > 0:
    print("Adolescente")
elif edad < 28 and edad > 0:
    print("Adulto")
elif edad > 60 and edad < 100:
    print("Persona mayor")
else :
    print("Edad no válida")
