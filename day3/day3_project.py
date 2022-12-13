texto = input("Ingresa el texto que quieras: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra ").lower())
letras.append(input("Ingresa la segunda letra ").lower())
letras.append(input("Ingresa la tercera letra ").lower())

print("\n")
print("Cantidad de letras:")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_letras3} veces")

print("\n")
print("Cantidad de palabras:")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras")

print("\n")
print("Letras de inicio y de fin:")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La primera letra es: '{letra_inicio}' y la última es '{letra_fin}'")

print("\n")
print("Texto invertido:")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"Texto invertido: {texto_invertido}")

print("\n")
print("Buscador de palabras:")
buscar_python = 'python' in texto
dict = {True: "Si", False: "No"}
print(f"¿Se encuentra la palabra 'python' en el texto? {dict[buscar_python]}")
