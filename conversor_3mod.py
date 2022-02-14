menu = """ 
Bienvenido al conversor de monedas 
1 - Pesos colombianos 
2 - Pesos argentinos    
3 - Pesos mexicanos

Elige una opcion
 """
opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3953.88
    dolares = pesos / valor_dolar
    dolares = round(dolares,2 )
    dolares = str(dolares)
    print("tienes $" + dolares + "dolares")
elif opcion == 2:
    pesos = input("¿cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 105.81
    dolares = pesos / valor_dolar
    dolares = round(dolares,2 )
    dolares = str(dolares)
    print("tienes $" + dolares + "dolares")
elif opcion == 3:
    pesos = input("¿cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20.61
    dolares = pesos / valor_dolar
    dolares = round(dolares,2 )
    dolares = str(dolares)
    print("tienes $" + dolares + "dolares")
else: 
    print("por favor digite una opcion correcta")