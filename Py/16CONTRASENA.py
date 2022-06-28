import random

# In this function we use [] to create lists, which contain several objects at the same time)
def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = [] #se define contrasena, como una lista, vacia inicialmente.

    for i in range(15): #un ciclo for hasta el numero de caracteres, 15.
        caracter_random = random.choice(caracteres) #método choice, del import random selecciona un valor de la lista ingresada
        contrasena.append(caracter_random) #con método append, agregamos valores al final de la lista.
    
    contrasena = "".join(contrasena) #convierte una lista completa a un string.
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es ' + contrasena)

if __name__ == '__main__':
    run()