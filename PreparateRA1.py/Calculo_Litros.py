def calcular_ganancia():
    while True:
        try:
            L = float(input("Ingrese la cantidad de litros producidos (debe ser un número positivo): "))
            if L < 0:
                print("Error: La cantidad de litros debe ser un número positivo.")
                continue
            PG = float(input("Ingrese el precio por galón (debe ser un número positivo): "))
            if PG < 0:
                print("Error: El precio por galón debe ser un número positivo.")
                continue
            break  # Si llegamos aquí, los valores son válidos y salimos del bucle de validación
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    TG = L / 3.785
    GA = PG * TG

    print("La ganancia es:", GA)

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Calcular ganancia")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calcular_ganancia()
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija 1 o 2.")

main()
