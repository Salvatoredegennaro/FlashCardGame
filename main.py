from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict ={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")



def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(letter_title, text="French", fill="black")
    canvas.itemconfig(letter2, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=image1)
    flip_timer = window.after(3000, func=flip_card)


def delete():
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def flip_card():
    canvas.itemconfig(canvas_image, image=image2)
    canvas.itemconfig(letter_title, text="English", fill="white")
    canvas.itemconfig(letter2, text=current_card["English"], fill="white")


window = Tk()
window.title("Flash Card Game")
window.minsize(width=800, height=700)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)
image1 = PhotoImage(file="images/card_front.png")
image2 = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=image1)

letter_title = canvas.create_text(400, 150, text="Title", font=("Aerial", 40, "italic"))
letter2 = canvas.create_text(400, 263, text="Word", font=("Aerial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

my_image = PhotoImage(file="images/wrong.png")
button = Button(image=my_image, highlightthickness=0, command=next_word)
button.grid(row=1, column=0)

my_image2 = PhotoImage(file="images/right.png")
button2 = Button(image=my_image2, highlightthickness=0, command=delete)
button2.grid(row=1, column=1)

next_word()

window.mainloop()
