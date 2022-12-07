texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[2:10:2]
print(fragmento)

fragmento = texto[::2]
print(fragmento)

frase = "Controlar la complejidad es la esencia de la programación"
palabra = frase[0:8]
print(palabra)

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
resultado = frase[8::3]
print(resultado)

# invert the string characters
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado = frase[::-1]
print(resultado)