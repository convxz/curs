from tkinter import *
from tkinter import filedialog
import numpy as np


def read_equations_from_file(file_path):
    """
    Чтение уравнений из файла.

    Аргументы:
    - file_path: путь к файлу с уравнениями

    Возвращает:
    - Список строк с уравнениями

    Исключения:
    - Если возникла ошибка при чтении файла
    """
    try:
        with open(file_path, 'r') as file:
            equations = file.readlines()

        equations = [eq.strip() for eq in equations]
        return equations
    except Exception as e:
        raise Exception(f"Ошибка при чтении уравнений из файла: {str(e)}")


def extract_coefficients_and_constants(equations):
    """
    Извлечение коэффициентов и свободных членов из уравнений.

    Аргументы:
    - equations: список строк с уравнениями

    Возвращает:
    - Коэффициенты уравнений в виде списка списков
    - Свободные члены в виде списка

    Пример:
    equations = ['2 3 4 = 10', '1 -1 1 = 5', '3 1 -2 = 1']
    coefficients, constants = extract_coefficients_and_constants(equations)
    # coefficients = [[2.0, 3.0, 4.0], [1.0, -1.0, 1.0], [3.0, 1.0, -2.0]]
    # constants = [10.0, 5.0, 1.0]
    """
    coefficients = []
    constants = []
    for eq in equations:
        parts = eq.split('=')
        coefficients.append([float(coef) for coef in parts[0].split()])
        constants.append(float(parts[1]))

    return coefficients, constants


def solve_linear_equations(coefficients, constants):
    """
    Решение системы линейных уравнений.

    Аргументы:
    - coefficients: коэффициенты уравнений в виде списка списков
    - constants: свободные члены уравнений в виде списка

    Возвращает:
    - Решение системы уравнений в виде списка значений переменных

    Исключения:
    - Если система уравнений не имеет решения
    """
    coefficients_matrix = np.array(coefficients)
    constants_vector = np.array(constants)

    try:
        solution = np.linalg.solve(coefficients_matrix, constants_vector)
        print(np.allclose(np.dot(coefficients_matrix, solution), constants_vector))
        if np.allclose(np.dot(coefficients_matrix, solution), constants_vector):
            return solution
        else:
            return False
    except np.linalg.LinAlgError:
        raise Exception("Невозможно решить систему линейных уравнений.")


def display_solution(solution):
    """
    Отображение решения системы уравнений.

    Аргументы:
    - solution: список значений переменных

    Выводит решение на экран.
    """
    solution_text.delete(1.0, END)
    for i, value in enumerate(solution):
        solution_text.insert(END, f'x{i+1} = {value:.3f}\n')


def solve_equations():
    """
    Обработчик кнопки "Select Equations File".

    Открывает диалоговое окно выбора файла с уравнениями.
    Читает уравнения из файла, решает систему линейных уравнений
    и отображает решение.
    """
    file_path = filedialog.askopenfilename()

    if file_path:
        try:
            equations = read_equations_from_file(file_path)
            coefficients, constants = extract_coefficients_and_constants(equations)
            solution = solve_linear_equations(coefficients, constants)
            display_solution(solution)
        except Exception as e:
            solution_text.delete(1.0, END)
            solution_text.insert(END, f'Ошибка: {str(e)}')
    else:
        solution_text.delete(1.0, END)
        solution_text.insert(END, 'Файл не выбран.')


if __name__ == "__main__":
    # Создание главного окна и других элементов GUI
    root = Tk()
    root.title('Linear Equation Solver')

    equation_frame = Frame(root)
    equation_frame.pack(pady=10)

    select_button = Button(equation_frame, text='Выбрать файл с уравнениями', command=solve_equations)
    select_button.pack(side=LEFT, padx=10)

    solution_text = Text(root, height=10, width=50)
    solution_text.pack(pady=10)

    root.mainloop()
