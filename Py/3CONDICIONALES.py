# Clase 14: condicionales - Ejercicio 1 uso de If
# edad = int(input("Escibre tu edad: "))  #adding the int before input, we are converting the input value
#                                         # w/o having to add another line to do the conversion of type
# if edad > 17: 
#     print("Eres mayor de edad.") 
# else:
#     print("Eres menor de edad.")

# Ejercicio 2 - Uso de Elif
numero = int(input("Escribe un número."))

if numero > 5: 
    print('Es mayor a 5')
elif numero == 5: # Elif es un condicional addicional de chequeo en IF. == se usa para comparación de variables
    print('Es igual a 5')
else: # Else se usa cuando no se cumplieron las condiciones anteriores en cualquier otro caso
    print('Es menor a 5')
