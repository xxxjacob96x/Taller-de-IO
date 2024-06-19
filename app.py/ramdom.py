"""
se quiere realizar una programacion, con el fin de ingresar y te entregue un campeon 
aleatorio del lol con la con dicion de que el campeon 1 sea igual a atrox 

"""
"""
import random

# Cadena de campeones separados por comas
champions_string = "Ahri, Akali, Alistar, Amumu, Anivia, Annie, Ashe, Aurelion Sol, Azir, Bard, Blitzcrank, Brand, Braum, Caitlyn, Camille, Cassiopeia, Cho'Gath, Corki, Darius, Diana, Draven, Dr. Mundo, Ekko, Elise, Evelynn, Ezreal, Fiddlesticks, Fiora, Fizz"

# Separar la cadena en una lista de campeones
champions_list = champions_string.split(", ")

# Seleccionar un campeón aleatorio de la lista
random_champion = random.choice(champions_list)

# Mostrar el campeón seleccionado
print(f"Campeón seleccionado: {random_champion}")


"""

import random

def main():
    # Cadena de campeones separados por comas (excluyendo a Aatrox)
    champions = "Ahri, Akali, Alistar, Amumu, Anivia, Annie, Ashe, Aurelion Sol, Azir, Bard, Blitzcrank, Brand, Braum, Caitlyn, Camille, Cassiopeia, Cho'Gath, Corki, Darius, Diana, Draven, Dr. Mundo, Ekko, Elise, Evelynn, Ezreal, Fiddlesticks, Fiora, Fizz"
    champions_list = champions.split(", ")

    while True:
        # Mostrar el menú
        print("\nMenú:")
        print("1. Mostrar Aatrox")
        print("2. Mostrar un campeón aleatorio")
        print("3. Salir")

        # Leer la opción del usuario
        choice = input("\nSelecciona una opción (1, 2, 3): ")

        if choice == '1':
            print("\nCampeón seleccionado: Aatrox")
        elif choice == '2':
            random_champion = random.choice(champions_list)
            print(f"\nCampeón seleccionado: {random_champion}")
        elif choice == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()

"""
import random

# Lista de 30 campeones incluyendo Aatrox como el primero
champions = [
    "Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "Aurelion Sol", "Azir",
    "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius",
    "Diana", "Draven", "Dr. Mundo", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz"
]

# Seleccionar un campeón aleatorio excluyendo a Aatrox
random_champion = random.choice(champions[1:])

# Mostrar el campeón seleccionado
print(f"Campeón seleccionado: {random_champion}")
"""


