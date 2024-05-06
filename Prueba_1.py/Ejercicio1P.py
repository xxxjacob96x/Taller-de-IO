def mostrar_menu():
    print("1. Ingresar pago por hora")
    print("2. Ingresar horas totales trabajadas")
    print("3. Calcular sueldo semanal")
    print("4. Calcular sueldo mensual")
    print("5. Salir")

def main():
    PH = 0
    HT = 0
    SH = 0

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            PH = int(input("Ingrese el pago por hora: "))
        elif opcion == "2":
            try:
                HT = int(input("Ingrese las horas totales trabajadas: "))
            except ValueError:
                print("Error: Por favor ingrese un número entero.")
        elif opcion == "3":
            SH = HT * PH
            print("El sueldo semanal es:", SH)
        elif opcion == "4":
            SU = SH * 4  # Suponiendo que la semana laboral es de 6 días
            print("El sueldo mensual es:", SU)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()
