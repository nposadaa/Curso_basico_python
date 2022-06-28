dolar = input("¿Cuántos dólares tienes?:") #input statement creates a question to user.
dolar = float(dolar) #float defines that the variable within () is a Decimal.
valor_dolar = 3875
pesos = dolar * valor_dolar #operación matemática para la conversión
pesos = round(pesos, 2) #round rounds a float value to a given amount of decimals.
pesos = str(pesos) #str defines that the variable is defined as text string
dolar = str(dolar)
print("Tienes $" + pesos + " pesos para los " + dolar + " que tienes.") #print the line with concatenation of text and variables.