from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)
canvas.create_text((400,150), text="Title", font=("Ariel", 40, "italic"))
canvas.create_text((400, 263), text="Word", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_button_image)
right_button = Button(image=right_button_image)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)



window.mainloop()
