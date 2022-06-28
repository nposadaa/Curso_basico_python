pesos = input("¿Cuántos persos tienes?:") #input statement creates a question to user.
pesos = float(pesos) #float defines that the variable within () is a Decimal.
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2) #round rounds a float value to a given amount of decimals.
dolares = str(dolares) #str defines that the variable is defined as text string
pesos = str(pesos)
print("Tienes $" + dolares + " dólares para los " + pesos + " que tienes.") #print the line with concatenation of text and variables.