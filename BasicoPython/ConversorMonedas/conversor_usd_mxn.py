pesos = input("¿Cuántos dólares tienes? ")
pesos = float(pesos)
valor_dolar = 20
pesos = pesos * valor_dolar
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")