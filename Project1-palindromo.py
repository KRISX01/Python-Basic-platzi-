def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("escirbe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("La palabra ingresada es palindromo")
    else:
        print("La palabra ingresada no es palindromo")


if __name__ == '__main__':
    run()

