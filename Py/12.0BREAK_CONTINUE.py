def run():
    # for contador in range(1000):
    #     if contador % 2 != 0: #divide los números en 2, y el reciduo de la división cuando es 0 es par, y cuando no es impar
    #         continue #con este statement pasa al siguiente indice del loop sin ejecutar lo que sigue.
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break #el programa irá imprimiendo cada una de los valores hasta que es igual al valor, y el break para.

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()
