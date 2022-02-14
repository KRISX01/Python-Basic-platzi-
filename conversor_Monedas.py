pesos = input("Por favor ingrese un valor en pesos a convertir: ")
pesos = float(pesos)
valor_dolar = 3956
dolares = pesos/valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("Tienes $" + dolares + "dolares")