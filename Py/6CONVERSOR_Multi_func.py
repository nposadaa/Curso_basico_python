menu = """
Bienvenido al conversor de monedas 💰

COP - Pesos colombianos
ARS - Pesos argentinos
MXN - Pesos mexicanos

Elige una opción: """ #triple comilla doble: permite crear un string de varias líneas. 😎

opcion = input(menu)

def conversor(opcion, valor_dolar):
    pesos = input("¿Cuántos pesos " + opcion + " tienes?: ") #input statement creates a question to user.
    pesos = float(pesos) #float defines that the variable within () is a Decimal.
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #round rounds a float value to a given amount of decimals.
    dolares = str(dolares) #str defines that the variable is defined as text string
    pesos = str(pesos)
    print("Tienes $" + dolares + " dólares para " + pesos + " a una tasa de 1 USD / " + str(valor_dolar) + " " + opcion) #print the line with concatenation of text and variables.

if opcion == 'COP':
    conversor(opcion, 4000)
elif opcion == 'ARS':
    conversor(opcion, 102)
elif opcion == 'MXN':
    conversor(opcion, 20)
else: print("Ingrese una opción válida, conchatumae.")