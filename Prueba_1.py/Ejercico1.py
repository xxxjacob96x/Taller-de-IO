# Crear una lista para almacenar las horas trabajadas en cada día
horas_por_dia = []

# Leer el pago por hora
PH = int(input("Ingrese el pago por hora: "))

# Leer las horas trabajadas para cada día de la semana
for dia in range(1, 7):  # 1 al 6 (inclusive)
    horas = int(input("Ingrese las horas trabajadas del día {}: ".format(dia)))
    horas_por_dia.append(horas)  # Agregar las horas a la lista

# Calcular el total de horas laboradas sumando las horas de la lista
SH = sum(horas_por_dia)

# Calcular el sueldo
SU = SH * PH

# Mostrar resultados
print("Las horas laboradas son =", SH)
print("El sueldo es =", SU)
 