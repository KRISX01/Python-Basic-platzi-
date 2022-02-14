def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("tienes $" + dolares + "dolares")
  

menu = """
Bienvenido al conversor de monedas 
1 - Pesos colombianos 
2 - Pesos argentinos    
3 - Pesos mexicanos

Elige la opcion que deseas
 """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Por favor ingresa una opcion correcta")