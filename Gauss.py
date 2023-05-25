import numpy as np
import tkinter as tk
from tkinter import ttk


def eliminate_zeros(matrix):
    def swap_rows(matrix, row1, row2):
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    swap_rows(matrix, i, j)
                    break
    return matrix


def gauss(a: np.zeros) -> np.zeros:
    """
    Функция будет решать уравнения методом Гаусса
    :param a: расширенная матрица
    :return: массив с решениями уравнения в случае, если верны входные данные и не происходит деления на 0, иначе None
    """
    n = len(a)
    x = np.zeros(n)
    a = eliminate_zeros(a)
    for i in range(n):
        if a[i][i] == 0.0:
            return None
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    return x


class Main(tk.Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.m = ttk.Entry(root, font='Century 12', width=20)
        self.m.pack(anchor=tk.NW)
        self.n = ttk.Entry(root, font='Century 12', width=20)
        self.n.pack(pady=5, anchor=tk.NW)
        self.enter = ttk.Button(text="Enter", command=self.get_vals)
        self.enter.pack()

        # b = ttk.Button(root, text="Enter", command=)  !!! надо создать команду, которая будет сохранять значения из m
        # и n и решать систему уравнений

    def get_vals(self):
        m = self.m.get()
        n = self.n.get()
        self.n.destroy()
        self.m.destroy()
        self.enter.destroy()
        self.n = n
        self.m = m
        self.res = ttk.Button(text="Reset", command=self.reset)
        self.res.pack()

    def reset(self):
        self.m = ttk.Entry(root, font='Century 12', width=20)
        self.m.pack(anchor=tk.NW)
        self.n = ttk.Entry(root, font='Century 12', width=20)
        self.n.pack(pady=5, anchor=tk.NW)
        self.enter = ttk.Button(text="Enter", command=self.get_vals)
        self.enter.pack()
        self.res.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root["bg"] = "#cfd47d"
    root.geometry("600x400+300+100")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
