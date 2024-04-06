Y = float(input("Ingrese el valor de Y: "))

# Proceso
if 0 <= Y <= 10:
    resultado = 4/Y - Y
elif 11 < Y <= 25:
    resultado = Y**3 - 12
elif 25 < Y <= 50:
    resultado = Y**2 + (Y**3 - 18)
else:
    resultado = 0

print("El valoe de X es:", resultado)
