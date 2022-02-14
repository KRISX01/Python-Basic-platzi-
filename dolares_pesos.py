dolares = input("Por favor ingrese el valor de dolares a convertir:   \n")
dolares = float(dolares)
valor_pesos = 0.00025278058
pesos = dolares/valor_pesos
pesos = round(pesos,2)
pesos = str(pesos)
print("el valor de los dolares que traes son: $" + pesos + "Pesos")