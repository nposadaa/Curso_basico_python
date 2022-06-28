# Dictionaries: to create a dictionary we use keys {}. It's a data structure of keys and values.

def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario) to print the whole dictionary.
    # print(mi_diccionario['llave1']) to print a line per each key.
    # print(mi_diccionario['llave2']) 
    # print(mi_diccionario['llave3']) 
    
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }
    # print(poblacion_paises['Argentina']) example of useful case

    # for pais in poblacion_paises.values(): how to print all in a list with a cycle
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes.')


if __name__ == '__main__':
    run()