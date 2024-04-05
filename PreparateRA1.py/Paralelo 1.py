import math

# Inicio del programa
R = float(input("Ingrese el valor de R: "))
H = float(input("Ingrese el valor de H: "))

C = math.sqrt(H**2 - R**2)
AT = (2 * R * C) / 2  # Esto podría simplificarse simplemente a R * C
AC = (math.pi * R**2) / 2
Area = AT + AC

print("El área es:", Area)
  

