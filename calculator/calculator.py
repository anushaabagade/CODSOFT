#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.

import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        op = operator_var.get()

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '/':
            result = a / b
        elif op == '*':
            result = a * b
        else:
            result = "Invalid Operation"
        
        result_label.config(text=f"Result: {a} {op} {b} = {result}")

    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math error", "Cannot divide by zero.")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operator_var.set("+")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Enter 1st Number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter 2nd Number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Choose Operation:").grid(row=2, column=0)

operator_var = tk.StringVar()
operator_var.set("+")

operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "/", "*")
operator_menu.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=3, column=1, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2, pady=10)

root.mainloop()
