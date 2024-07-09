# src/calculator.py
import tkinter as tk
from math import *

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

# GUI for calculator
def calculator_gui():
    root = tk.Tk()
    root.title("Calculator")

    expression = ""
    entry = tk.Entry(root, width=40, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=4)

    def button_click(number):
        nonlocal expression
        expression += str(number)
        entry.delete(0, tk.END)
        entry.insert(0, expression)

    def button_clear():
        nonlocal expression
        expression = ""
        entry.delete(0, tk.END)

    def button_equal():
        nonlocal expression
        result = evaluate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('C', 5, 0)
    ]

    for (text, row, col) in buttons:
        if text == '=':
            button = tk.Button(root, text=text, padx=40, pady=20, command=button_equal)
        elif text == 'C':
            button = tk.Button(root, text=text, padx=40, pady=20, command=button_clear)
        else:
            button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t))
        button.grid(row=row, column=col)

    root.mainloop()

# Test the calculator GUI
if __name__ == "__main__":
    calculator_gui()
