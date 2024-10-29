import random
import tkinter as tk
from tkinter import messagebox

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

def generate_password():
    try:
        nr_letters = int(letter_entry.get())
        nr_symbols = int(symbol_entry.get())
        nr_numbers = int(number_entry.get())
        
        password_list = []
        
        for _ in range(nr_letters):
            password_list.append(random.choice(letters))
        for _ in range(nr_symbols):
            password_list.append(random.choice(symbols))
        for _ in range(nr_numbers):
            password_list.append(random.choice(numbers))

        random.shuffle(password_list)
        password = ''.join(password_list)
        
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for letters, symbols, and numbers.")

window = tk.Tk()
window.title("PyPassword Generator")
window.geometry("400x300")
window.config(padx=20, pady=20)

tk.Label(window, text="Number of Letters:").grid(row=0, column=0, pady=5)
letter_entry = tk.Entry(window, width=10)
letter_entry.grid(row=0, column=1)

tk.Label(window, text="Number of Symbols:").grid(row=1, column=0, pady=5)
symbol_entry = tk.Entry(window, width=10)
symbol_entry.grid(row=1, column=1)

tk.Label(window, text="Number of Numbers:").grid(row=2, column=0, pady=5)
number_entry = tk.Entry(window, width=10)
number_entry.grid(row=2, column=1)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=20)

password_entry = tk.Entry(window, width=40)
password_entry.grid(row=4, column=0, columnspan=2, pady=5)

window.mainloop()
