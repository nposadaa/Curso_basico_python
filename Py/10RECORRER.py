#imprime cada letra en un expresión que escribe el usuario
def run():
    nombre = input('Escribre tu nombre: ')
    for letra in nombre: #in this case we use for with IN followed by a string.
        if letra == 'i':
            print('Es la i')
        else:
            print(letra)

if __name__ == '__main__':
    run()