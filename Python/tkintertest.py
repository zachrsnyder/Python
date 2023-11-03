from tkinter import *
from tkinter import ttk
import random

def open_settings(event):
    canvas_menu = Canvas(window, bg = "black", height=300, width=400)
    resume_button = Button(window, text="Resume Game", command=canvas_menu.destroy)
    canvas_menu.create_window(30,30,window=resume_button)
    canvas_menu.pack()


def start_game():
    title_label.destroy()
    start_button.destroy()
    settings_button.destroy()
    exit_button.destroy()
    canvas.pack()


window = Tk()
window.title("Game Start Menu")
window.geometry("400x300")

title_label = Label(window, text="Game Title", font=("Arial", 20))
start_button = Button(window, text="Start Game", command=start_game)
settings_button = Button(window, text="Settings", command=open_settings)
exit_button = Button(window, text="Exit", command=window.destroy)
canvas = Canvas(window, bg = "red", height=300, width=400)

title_label.pack(pady=70)
start_button.pack()
settings_button.pack()
exit_button.pack()

window.bind('<Down>', open_settings)

window.mainloop()


