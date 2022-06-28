import random #funciones nativas de python se llaman con import, en este caso random.

def run():
    randonnum = random.randint(1,100) #genera un randon int (un entero random),
    numeroele = int(input("Elige un número del 1 al 100: "))

    while numeroele != randonnum:
        if numeroele < randonnum:
            numeroele = int(input("Elige un número mayor: "))
        else:
            numeroele = int(input("Elige un número menor: "))
    print("Ganaste!")

if __name__ == '__main__':
    run()