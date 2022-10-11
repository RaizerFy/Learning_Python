from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA CONFIG ------------------------------- #
try:
    my_dict = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    my_dict = pd.read_csv("data/french_words.csv")

my_dict = my_dict.to_dict(orient="records")

card = {}


def next_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(my_dict)
    word_french = card["French"]
    # canvas.itemconfigure("Language", text=f"{language}")
    canvas.itemconfigure(canvas_image, image=front_image)
    canvas.itemconfigure(text_1, text="French", fill="black")
    canvas.itemconfigure(text_2, text=f"{word_french}", fill="black")
    window.after(3000, func=flip_card)


def flip_card():
    word_english = card["English"]
    canvas.itemconfigure(canvas_image, image=back_image)
    canvas.itemconfigure(text_1, text="English", fill="white")
    canvas.itemconfigure(text_2, text=f"{word_english}", fill="white")


def if_right():
    my_dict.remove(card)
    next_card()


def if_wrong():
    next_card()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
text_1 = canvas.create_text((400, 150), text="Title", font=("Ariel", 40, "italic"), tags="-LANGUAGE-")
text_2 = canvas.create_text((400, 263), text="Word", font=("Ariel", 40, "bold"), tags="-WORD-")
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_button_image, command=if_wrong)
right_button = Button(image=right_button_image, command=if_right)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()

df = pd.DataFrame(my_dict)
df.to_csv("data/words_to_learn.csv", index=False)


