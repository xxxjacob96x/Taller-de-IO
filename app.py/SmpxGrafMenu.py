import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

def plot_constraints(x_values, constraints, labels):
    for constraint, label in zip(constraints, labels):
        y_values = [constraint(x) for x in x_values]
        plt.plot(x_values, y_values, label=label)
        plt.fill_between(x_values, 0, y_values, where=(np.array(y_values) >= 0), alpha=0.3)


def get_input():
    num_vars = int(input("Ingrese la cantidad de variables: "))
    objective = input("¿Desea maximizar (max) o minimizar (min)? ").lower()
    return num_vars, objective

def solve_optimization(num_vars, objective):
    c = [-1 if objective == 'min' else 1] * num_vars  # Coeficientes de la función objetivo

    A_ub = []  # Coeficientes de las restricciones <=
    b_ub = []  # Lados derechos de las restricciones <=
    constraints = []  # Funciones de restricción

    for i in range(num_vars):
        constraint_expr = input(f"Ingrese la restricción {i+1} (en términos de x{i+1}): ")
        A_row = [int(coeff) for coeff in constraint_expr.split()]
        A_ub.append(A_row)

        b_val = float(input(f"Ingrese el lado derecho de la restricción {i+1}: "))
        b_ub.append(b_val)

        def constraint_func(x_val, A_row=A_row, b_val=b_val):
            x_val_list = list(x_val) if isinstance(x_val, np.ndarray) else x_val  # Convertir x_val a lista si es un array de numpy
            sum_product = sum(A_row[j] * x_val_list[j] for j in range(len(x_val_list)))
            return (b_val - sum_product) / A_row[i] if A_row[i] != 0 else np.nan


        constraints.append(constraint_func)

    bounds = [(0, None)] * num_vars  # Límites de las variables (x1, x2, ...)
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    return result, constraints

def main():
    while True:
        plt.clf()  # Limpiar la figura anterior
        num_vars, objective = get_input()
        result, constraints = solve_optimization(num_vars, objective)

        x_values = np.linspace(0, 10, 100)  # Valores de x para graficar
        plot_constraints(x_values, constraints, [f"Restricción {i+1}" for i in range(num_vars)])
        plt.scatter(*[result.x[i] for i in range(num_vars)], color='red', label='Punto óptimo')
        plt.xlabel("x1")
        plt.ylabel("x2, x3, ...")
        plt.title("Región Factible y Punto Óptimo")
        plt.legend()
        plt.show()

        cont = input("¿Desea resolver otro ejercicio? (s/n): ")
        if cont.lower() != 's':
            break

if __name__ == "__main__":
    main()
