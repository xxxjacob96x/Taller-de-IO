""" 
Crear un programa para gestionar la informacion de empleados en una empresa.
El sistema permitira resgistrar empleados con su nombre, edad y salario.
Ademas, debera mostrar la lista de empleados de manera ordenada, incluyendo su edad y
salario y el promedio de edades y salarios

"""

Empleados = []

while True: 
    print(""" 
          ======= Registro de Empleados =======
          1. Registrar empleados
          2. Mostrar todo los empleados
          3. Salir 
          """)
    
    Opcion = int(input("Ingrese su opcion (1 o 2 o precione cualquier tecla para salir): "))

    if Opcion == 1:
        nombre = input("ngrese el nombre del empleado: ")
        edad = int(input("Ingrse la edad del empleado: "))