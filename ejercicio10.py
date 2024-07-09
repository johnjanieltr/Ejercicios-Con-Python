frase = input("Ingrese una frase: ")

contador_vocales = 0

for letra in frase:
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    contador_vocales += 1

if contador_vocales > 1:
  print(f'La frase "{frase}" tiene {contador_vocales} vocales')
else:
  print(f'La frase "{frase}" tiene una vocal')
