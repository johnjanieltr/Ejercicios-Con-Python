lista_numeros = [10, 50, 22, 35, 9]

numero_grande = 0

for num in lista_numeros:
  if num > numero_grande:
    numero_grande = num

print(f"El numero mas grande de la lista es el {numero_grande}")