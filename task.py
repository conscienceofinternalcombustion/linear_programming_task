import numpy as np
from scipy.optimize import linprog

# Запросить количество переменных
num_variables = int(input("Введите количество переменных: "))

# Запросить коэффициенты целевой функции
obj_coeffs = []
for i in range(num_variables):
    coeff = float(input(f"Введите коэффициент целевой функции для переменной {i+1}: "))
    obj_coeffs.append(coeff)

# Запросить тип задачи (максимизация или минимизация)
problem_type = input("Введите тип задачи (максимизация или минимизация): ")

# Запросить количество ограничений
num_constraints = int(input("Введите количество ограничений: "))

# Запросить коэффициенты ограничений
A = []
b = []
for i in range(num_constraints):
    coeffs = []
    for j in range(num_variables):
        coeff = float(input(f"Введите коэффициент ограничения {i+1} для переменной {j+1}: "))
        coeffs.append(coeff)
    constraint_value = float(input(f"Введите значение ограничения {i+1}: "))
    A.append(coeffs)
    b.append(constraint_value)

# Запросить типы ограничений (<=, =, >=)
constraint_types = []
for i in range(num_constraints):
    constraint_type = input(f"Введите тип ограничения {i+1} (<=, =, >=): ")
    constraint_types.append(constraint_type)

# Преобразовать тип задачи в формат, понятный linprog
if problem_type.lower() == "максимизация":
    problem_type = "max"
elif problem_type.lower() == "минимизация":
    problem_type = "min"

# Преобразовать типы ограничений в формат, понятный linprog
constraint_types_dict = {"<=": "leq", "=": "eq", ">=": "geq"}
constraint_types = [constraint_types_dict[ctype] for ctype in constraint_types]

# Решить задачу линейного программирования
result = linprog(c=obj_coeffs, A_ub=A, b_ub=b, A_eq=None, b_eq=None, method="simplex")

# Вывести результаты
if result.success:
    print("Оптимальное решение найдено:")
    print("Значение целевой функции:", result.fun)
    print("Значения переменных:")
    for i, value in enumerate(result.x):
        print(f"Переменная {i+1}: {value}")
else:
    print("Решение не найдено.")
