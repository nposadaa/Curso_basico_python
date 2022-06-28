# abajo un emjemplo que cómo se escribe una función en Python
# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones: ')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

opcion = int(input('Elige una opción (1, 2, 3): '))

def conversacion():
    opcion_str = str(opcion)
    print('Hola! Cómo estás?')
    print('Elegiste la opción ' + opcion_str +' . Adios!')
if opcion == 1:
    conversacion()
elif opcion == 2:
    conversacion()
elif opcion == 3:
    conversacion()
else:
    print('Escribe la opción correcta')