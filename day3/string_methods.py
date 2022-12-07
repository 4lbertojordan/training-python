texto = "Este es el texto de Alberto"

resultado = texto.upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.split("t")
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "fácil"
e = " ".join([a, b, c, d])

print(e)


resultado = texto.find("A")
print(resultado)

resultado = texto.replace("Alberto", "Juan")
print(resultado)

resultado = texto.replace("e", "o")
print(resultado)

texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
# reemplazar difícil por fácil y mala por buena
resultado = texto.replace("difícil", "fácil").replace("mala", "buena")
print(resultado)

