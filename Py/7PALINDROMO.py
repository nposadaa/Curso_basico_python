# Palíndromo: una palabra o frase que se lee igual de adelante a atras. Ej: Luz Azul.
def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindrono = palindromo(palabra)
    if es_palindrono == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")       


if __name__ == '__main__':
    run()
