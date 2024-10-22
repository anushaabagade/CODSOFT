import tkinter as tk
import random
from PIL import Image, ImageTk

def determine_winner(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.randint(0, 2)

    if user_choice == computer_choice:
        result = "Draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        result = "You won!"
    else:
        result = "You lost!"

    result_label.config(text=f"You chose: {options[user_choice]}\nComputer chose: {options[computer_choice]}\n{result}")

    user_image_label.config(image=game_images[user_choice])
    computer_image_label.config(image=game_images[computer_choice])

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("600x600")
window.config(bg="#282c34")


rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((150, 150)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((150, 150)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((150, 150)))


game_images = [rock_img, paper_img, scissors_img]

title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Helvetica", 24), bg="#282c34", fg="#61dafb")
title_label.pack(pady=20)

rock_button = tk.Button(window, text="Rock", command=lambda: determine_winner(0), width=15, height=2)
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", command=lambda: determine_winner(1), width=15, height=2)
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", command=lambda: determine_winner(2), width=15, height=2)
scissors_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 16), bg="#282c34", fg="white")
result_label.pack(pady=20)

user_image_label = tk.Label(window, bg="#282c34")
user_image_label.pack(side=tk.LEFT, padx=20)

computer_image_label = tk.Label(window, bg="#282c34")
computer_image_label.pack(side=tk.RIGHT, padx=20)

window.mainloop()
