def es_palindromo(texto):
    texto = texto.lower()
    limpio = ""
    for caracter in texto:
        if caracter != " ":
            limpio += caracter
    return limpio == limpio[::-1], limpio

entrada = input("Ingresa una frase o palabra: ")
resultado, cadena_limpia = es_palindromo(entrada)

if resultado:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
print("Longitud de la cadena limpia:", len(cadena_limpia))