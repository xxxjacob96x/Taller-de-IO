L = float(input("Ingrese la cantidad de litros producidos: "))
PG = float(input("Ingrese el precio por galón: "))

TG = L / 3.785  # Calcula la cantidad de galones producidos
GA = PG * TG     # Calcula la ganancia por la entrega de leche

print("La ganancia es:", GA)
# Fin del programa
