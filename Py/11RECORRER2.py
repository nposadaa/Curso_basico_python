#imprime cada letra en un expresión que escribe el usuario en mayúsculas
def run():
    frase = input('Escribre una frase: ')
    for caracter in frase:
        print(caracter.upper())

if __name__ == '__main__':
    run()