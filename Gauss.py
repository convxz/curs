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
        self.test = ttk.Button(text="tests", command=self.tests)
        self.test.pack()

        # b = ttk.Button(root, text="Enter", command=)  !!! надо создать команду, которая будет сохранять значения из m
        # и n и решать систему уравнений

    def tests(self):
        self.test.destroy()
        self.n.destroy()
        self.m.destroy()
        self.enter.destroy()
        x1 = np.zeros((2, 3))
        x1[0][0], x1[0][1], x1[0][2], x1[1][0], x1[1][1], x1[1][2] = 1, -1, -5,  0, 1, 1
        x2 = np.zeros((2, 3))
        x2[0][0], x2[0][1], x2[0][2], x2[1][0], x2[1][1], x2[1][2] = 3, 2, 2, 4, 1, 6
        x3 = np.zeros((2, 3))
        x3[0][0], x3[0][1], x3[0][2], x3[1][0], x3[1][1], x3[1][2] = 1, -1, 4, 1, 2, 10
        x4 = np.zeros((2, 3))
        x4[0][0], x4[0][1], x4[0][2], x4[1][0], x4[1][1], x4[1][2] = 1, 5, 7, 3, 4, 2
        self.x1_l = ttk.Label(text=f"{x1} -> {gauss(x1)}")
        self.x2_l = ttk.Label(text=f"{x2} -> {gauss(x2)}")
        self.x3_l = ttk.Label(text=f"{x3} -> {gauss(x3)}")
        self.x4_l = ttk.Label(text=f"{x4} -> {gauss(x4)}")
        self.x1_l.pack(anchor=tk.NW)
        self.x2_l.pack(anchor=tk.NW)
        self.x3_l.pack(anchor=tk.NW)
        self.x4_l.pack(anchor=tk.NW)
        self.res_test = ttk.Button(text="Reset", command=self.res_tests)
        self.res_test.pack()

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

    def res_tests(self):
        self.x1_l.destroy()
        self.x2_l.destroy()
        self.x3_l.destroy()
        self.x4_l.destroy()
        self.m = ttk.Entry(root, font='Century 12', width=20)
        self.m.pack(anchor=tk.NW)
        self.n = ttk.Entry(root, font='Century 12', width=20)
        self.n.pack(pady=5, anchor=tk.NW)
        self.enter = ttk.Button(text="Enter", command=self.get_vals)
        self.enter.pack()
        self.test = ttk.Button(text="tests", command=self.tests)
        self.test.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root["bg"] = "#cfd47d"
    root.geometry("600x400+300+100")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
